import collections

def if_contains_anagrams(words):
    anagrams = collections.defaultdict(lambda: collections.Counter())
    for word in words:
        if len(word) >= 3:
            anagrams[''.join(sorted(word.lower()))].append(word)
    return len(list(filter(lambda anagram_group: len(anagram_group) > 1, anagrams.values()))) <= 257