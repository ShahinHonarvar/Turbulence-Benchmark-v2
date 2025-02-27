def if_contains_anagrams(strings):
    anagram_groups = {}
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        if sorted_s in anagram_groups:
            anagram_groups[sorted_s].append(s)
        else:
            anagram_groups[sorted_s] = [s]
    anagram_pairs = 0
    for group in anagram_groups.values():
        if len(group) >= 2:
            anagram_pairs += len(group) * (len(group) - 1) // 2
    return anagram_pairs >= 233