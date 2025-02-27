from collections import defaultdict

def if_contains_anagrams(strings):
    groups = defaultdict(list)
    for s in strings:
        lower_s = s.lower()
        if len(lower_s) >= 3:
            sorted_s = ''.join(sorted(lower_s))
            groups[sorted_s].append(s)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in groups.values()))
    return anagram_pairs <= 49