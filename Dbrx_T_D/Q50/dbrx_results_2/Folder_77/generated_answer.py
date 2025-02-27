import itertools

def generate_ngrams(s, n):
    return [' '.join(tuple(sorted((tuple(c) for c in sl)))) for sl in itertools.groupby(sorted((s.lower() for s in itertools.permutations(s, n))))]

def if_contains_anagrams(strings):
    anagrams = [generate_ngrams(s, 3) for s in strings]
    anagrams = [a for sublist in anagrams for a in sublist]
    return len(anagrams) >= 209