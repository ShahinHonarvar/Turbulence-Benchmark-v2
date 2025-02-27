import itertools

def palindromes_between_indices(s):
    letters = ''.join([c for c in s[4:10] if c.isalpha()]).lower()
    permutations = set(itertools.permutations(letters, 7))
    palindromes = {''.join(p) for p in permutations if ''.join(p) == ''.join(p)[::-1]}
    return palindromes