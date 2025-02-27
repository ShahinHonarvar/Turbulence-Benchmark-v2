from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_sets = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_sets[sorted_str].append(s)
    anagram_pairs = 0
    for anagrams in anagram_sets.values():
        n = len(anagrams)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
    return anagram_pairs >= 411