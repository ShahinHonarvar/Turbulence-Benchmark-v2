from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(sorted(set(s[2:8])))
    palindromes = {''.join(p) + ''.join(p)[::-1] for i in range(6, len(letters) + 1) for p in permutations(letters, i)}
    return palindromes