import collections

def if_contains_anagrams(strings):
    anagrams = collections.defaultdict(list)
    for string in strings:
        anagram_key = tuple(sorted({char.lower() for char in string if char.isalpha()}))
        if len(anagram_key) >= 3:
            anagrams[anagram_key].append(string)
    return sum((1 for value in anagrams.values() if len(value) > 1)) <= 366