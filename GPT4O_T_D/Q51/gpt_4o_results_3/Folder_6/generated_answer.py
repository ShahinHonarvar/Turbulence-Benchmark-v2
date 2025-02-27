from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            normalized = ''.join(sorted(s.lower()))
            anagram_groups[normalized].append(s)
    total_pairs = 0
    for group in anagram_groups.values():
        n = len(group)
        if n > 1:
            total_pairs += n * (n - 1) // 2
            if total_pairs > 86:
                return False
    return True