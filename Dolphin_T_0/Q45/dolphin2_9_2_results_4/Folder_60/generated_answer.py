from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(sorted(s[3:7]))
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for p in permutations(letters, length):
            p = ''.join(p).lower()
            if p == p[::-1] and all((c.isalpha() for c in p)):
                palindromes.add(p)
    return palindromes