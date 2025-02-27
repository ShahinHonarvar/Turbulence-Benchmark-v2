import itertools

def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        sorted_s = tuple(sorted(s.lower()))
        if len(s) >= 3:
            anagrams[sorted_s] = anagrams.get(sorted_s, []) + [s]
    return len(list(itertools.combinations(anagrams.values(), 2))) >= 28