from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_groups[sorted_str] += 1
    return sum((v * (v - 1) // 2 for v in anagram_groups.values())) >= 81