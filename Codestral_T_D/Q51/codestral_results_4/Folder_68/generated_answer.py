from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            anagrams[''.join(sorted(string.lower()))].append(string)
    anagram_pairs = sum((len(anagrams[key]) * (len(anagrams[key]) - 1) // 2 for key in anagrams))
    return anagram_pairs <= 94