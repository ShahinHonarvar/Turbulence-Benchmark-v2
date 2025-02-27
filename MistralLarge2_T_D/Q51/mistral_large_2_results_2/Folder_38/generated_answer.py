from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_count[sorted_s].append(s)
    pairs_count = sum((len(group) * (len(group) - 1) // 2 for group in anagram_count.values()))
    return pairs_count <= 416