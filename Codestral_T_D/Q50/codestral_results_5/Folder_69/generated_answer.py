from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for word in strings:
        if len(word) >= 3:
            anagrams[''.join(sorted(word.lower()))].append(word)
    return sum((len(anagram) * (len(anagram) - 1) // 2 for anagram in anagrams.values())) >= 188