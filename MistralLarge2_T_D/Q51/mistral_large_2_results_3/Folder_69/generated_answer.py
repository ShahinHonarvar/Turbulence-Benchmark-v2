from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        anagram_count[sorted_s].append(s)
    pair_count = 0
    for group in anagram_count.values():
        if len(group) > 1:
            pair_count += len(group) * (len(group) - 1) // 2
    return pair_count <= 58