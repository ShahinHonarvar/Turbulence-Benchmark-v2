from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c for c in s[2:6] if c.isalpha()]).lower() + ''
    palindromes = set()
    for p in permutations(letters, 4):
        if ''.join(p) == ''.join(p)[::-1]:
            palindromes.add(''.join(p))
    return palindromes