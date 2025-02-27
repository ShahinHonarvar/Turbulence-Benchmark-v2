from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagrams[''.join(sorted(s.lower()))].append(s)
    return sum((len(anagram_group) * (len(anagram_group) - 1) // 2 for anagram_group in anagrams.values())) >= 59