from itertools import permutations, starmap
    from operator import mul
    from string import ascii_letters as alphabet

def palindromes_between_indices(s):
    s_alphabet = [c for c in s if c in alphabet]
    s_alphabet_set = set(s_alphabet)
    length = len(s_alphabet)
    r_palindromes = set()
    for l in range(4, length + 1):
        starmap(lambda a, b: r_palindromes.add(b), enumerate(permutations(s_alphabet_set, l)))
    r_palindromes = set((''.join(p) for p in r_palindromes if ''.join(p) == ''.join(reversed(p))))
    return r_palindromes