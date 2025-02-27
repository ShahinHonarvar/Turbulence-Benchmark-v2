from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_chars = ''.join(sorted(s.lower()))
            anagram_groups[sorted_chars].append(s)
    num_pairs = 0
    for group in anagram_groups.values():
        n = len(group)
        num_pairs += n * (n - 1) // 2
        if num_pairs > 401:
            return False
    return True