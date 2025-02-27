from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(sorted(s[4:9]))
    palindromes = set()
    for p in permutations(letters, 3):
        p = ''.join(p).lower()
        if p == p[::-1]:
            palindromes.add(p)
    return palindromes