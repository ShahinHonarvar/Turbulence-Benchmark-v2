from itertools import permutations

def palindromes_between_indices(s):
    s = s[:4].lower()
    palindromes = set()
    for p in permutations(s, 3):
        if p == p[::-1]:
            palindromes.add(''.join(p))
    return palindromes