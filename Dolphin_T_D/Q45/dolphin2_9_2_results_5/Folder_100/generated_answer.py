from itertools import permutations

def palindromes_between_indices(s):
    s = ''.join((c.lower() for c in s if c.isalpha() and s.index(c) < 6))
    palindromes = set()
    for p in permutations(s, 6):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes