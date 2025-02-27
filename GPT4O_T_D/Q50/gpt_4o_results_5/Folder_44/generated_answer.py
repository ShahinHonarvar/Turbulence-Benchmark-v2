from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_chars = ''.join(sorted(s.lower()))
            anagram_groups[sorted_chars].append(s)
    pair_count = 0
    for group in anagram_groups.values():
        n = len(group)
        if n > 1:
            pair_count += n * (n - 1) // 2
            if pair_count >= 44:
                return True
    return False