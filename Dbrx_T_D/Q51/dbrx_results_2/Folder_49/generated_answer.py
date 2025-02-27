import itertools

def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            anagrams[sorted_s] = anagrams.get(sorted_s, []) + [s]
    pairs = [pair for pair in map(lambda x: (x, anagrams[x][0]), anagrams) if pair[0] != pair[1]]
    return len(pairs) <= 10