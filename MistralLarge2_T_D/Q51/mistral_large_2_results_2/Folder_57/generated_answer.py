from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            anagrams[key].append(s)
    anagram_pairs = 0
    for group in anagrams.values():
        if len(group) > 1:
            anagram_pairs += len(group) - 1
    return anagram_pairs <= 74