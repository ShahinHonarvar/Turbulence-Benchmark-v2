from collections import Counter

def if_contains_anagrams(strings):
    anagram_groups = {}
    for s in strings:
        lower_s = s.lower()
        if len(lower_s) < 3:
            continue
        sorted_s = ''.join(sorted(lower_s))
        if sorted_s not in anagram_groups:
            anagram_groups[sorted_s] = []
        anagram_groups[sorted_s].append(s)
    anagram_count = 0
    for group in anagram_groups.values():
        if len(group) >= 2:
            anagram_count += len(group) * (len(group) - 1) // 2
    return anagram_count >= 18