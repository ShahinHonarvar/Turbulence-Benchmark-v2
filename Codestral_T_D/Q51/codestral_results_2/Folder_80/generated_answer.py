from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            anagram_groups[''.join(sorted(s_lower))].append(s)
    anagram_count = 0
    for group in anagram_groups.values():
        anagram_count += len(group) * (len(group) - 1) // 2
        if anagram_count > 255:
            return False
    return True