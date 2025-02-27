from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:10]]
    palindromes = set()
    for p in permutations(letters, 7):
        if ''.join(p) == ''.join(p)[::-1]:
            palindromes.add(''.join(p))
    return palindromes