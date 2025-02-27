import itertools

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    pairs = list(itertools.combinations(strings, 2))
    anagram_pairs = [(a, b) for a, b in pairs if sorted(a) == sorted(b) and len(a) >= 3]
    return len(anagram_pairs) <= 147