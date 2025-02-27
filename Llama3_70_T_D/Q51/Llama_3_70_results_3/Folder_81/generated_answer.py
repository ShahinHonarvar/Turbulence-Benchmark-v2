from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = defaultdict(int)
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_count[sorted_s] += 1
    return sum((count * (count - 1) // 2 for count in anagram_count.values())) <= 79