from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = defaultdict(int)
    for s in lst:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_count[sorted_s] += 1
    anagram_pairs = [c * (c - 1) // 2 for c in anagram_count.values() if c > 1]
    return sum(anagram_pairs) >= 115