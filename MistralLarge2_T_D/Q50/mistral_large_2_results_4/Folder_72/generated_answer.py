from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_count[sorted_s].append(s)
    pair_count = 0
    for key in anagram_count:
        n = len(anagram_count[key])
        pair_count += n * (n - 1) // 2
    return pair_count >= 55