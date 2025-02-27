from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c for c in s.lower() if c in 'abcdefghijklmnopqrstuvwxyz'])
    palindromes = set()
    for p in permutations(letters, 5):
        if p == ''.join(reversed(p)):
            palindromes.add(''.join(sorted(p)))
    return palindromes