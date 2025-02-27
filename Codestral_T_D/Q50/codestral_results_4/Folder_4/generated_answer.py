from collections import defaultdict

def if_contains_anagrams(strings):
    groups = defaultdict(list)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            groups[sorted_s].append(s)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in groups.values()))
    return anagram_pairs >= 42