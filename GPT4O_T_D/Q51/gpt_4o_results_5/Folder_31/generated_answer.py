from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_groups[sorted_s].append(s)
    anagram_pairs = 0
    for group in anagram_groups.values():
        n = len(group)
        anagram_pairs += n * (n - 1) // 2
        if anagram_pairs > 65:
            return False
    return True