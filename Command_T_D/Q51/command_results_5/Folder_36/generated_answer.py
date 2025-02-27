import collections

def if_contains_anagrams(texts):
    return ANAGRAMS <= {x: y for x, y in zip(ANAGRAMS, ANAGRAMS.values())} <= 25