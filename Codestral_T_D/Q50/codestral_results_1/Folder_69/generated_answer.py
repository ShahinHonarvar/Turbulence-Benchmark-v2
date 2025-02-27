from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagrams[''.join(sorted(s.lower()))].append(s)
    return any((len(anagram_group) >= 2 for anagram_group in anagrams.values()))