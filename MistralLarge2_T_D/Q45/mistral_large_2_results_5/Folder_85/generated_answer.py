from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[2:9] if c.isalpha()]
    palindromes = set()
    for length in range(7, len(letters) + 1):
        for perm in permutations(letters, length):
            p = ''.join(perm).lower()
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes