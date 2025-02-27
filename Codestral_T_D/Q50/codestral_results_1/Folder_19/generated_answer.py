from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            anagrams[''.join(sorted(string.lower()))].append(string)
    return sum((len(anagram_group) * (len(anagram_group) - 1) // 2 for anagram_group in anagrams.values())) >= 84