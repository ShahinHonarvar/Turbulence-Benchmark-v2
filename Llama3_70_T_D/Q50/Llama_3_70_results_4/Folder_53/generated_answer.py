from collections import defaultdict

def if_contains_anagrams(lst):
    count = defaultdict(int)
    anagram_count = 0
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            count[sorted_s] += 1
    for v in count.values():
        anagram_count += v * (v - 1) // 2
    return anagram_count >= 11