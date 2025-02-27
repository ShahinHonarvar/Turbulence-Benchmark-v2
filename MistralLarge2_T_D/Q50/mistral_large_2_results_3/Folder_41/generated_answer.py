from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(list)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            anagram_count[sorted_s].append(s)
    pair_count = sum((len(v) * (len(v) - 1) // 2 for v in anagram_count.values() if len(v) > 1))
    return pair_count >= 75