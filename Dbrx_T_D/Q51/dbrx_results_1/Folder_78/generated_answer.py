import collections

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        key = tuple(sorted(word.lower()))
        if len(key) >= 3:
            anagrams[key] = anagrams.get(key, []) + [word]
    return len(list(collections.ChainMap(*anagrams.values()).items())) <= 70