from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = defaultdict(int)
    for s in lst:
        s_lower = ''.join(filter(str.isalpha, s)).lower()
        if len(s_lower) >= 3:
            key = ''.join(sorted(s_lower))
            anagram_count[key] += 1
    return sum((x * (x - 1) // 2 for x in anagram_count.values())) <= 116