import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:10])).lower()
    permutations = set((''.join(p) for p in itertools.permutations(letters, 7)))
    palindromes = {p for p in permutations if p == p[::-1]}
    return palindromes