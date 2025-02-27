import itertools
    from collections import Counter

def palindromes_between_indices(string):
    english_letters = filter(str.isalpha, string[4:10])
    permutations = set((''.join(p) for p in itertools.permutations(english_letters)))
    palindromes = {p for p in permutations if Counter(p.lower()) == Counter(p.lower())}
    return palindromes