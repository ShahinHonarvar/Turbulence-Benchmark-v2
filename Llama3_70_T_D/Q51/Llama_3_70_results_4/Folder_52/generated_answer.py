from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = defaultdict(int)
    total_anagrams = 0
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        anagram_count[sorted_s] += 1
        total_anagrams += anagram_count[sorted_s] - 1
        if total_anagrams > 43:
            return False
    return True