from itertools import permutations

def palindromes_between_indices(s):
    eng_letters = [c for c in s[1:5] if c.isalpha()]
    if len(set(eng_letters)) < 5:
        return set()
    letters_permutations = [''.join(p) for p in permutations(eng_letters, len(eng_letters))]
    palindromes = {''.join([c for c in p if c.isalpha()]) for p in letters_permutations if p == p[::-1] and len(p) >= 5}
    return palindromes