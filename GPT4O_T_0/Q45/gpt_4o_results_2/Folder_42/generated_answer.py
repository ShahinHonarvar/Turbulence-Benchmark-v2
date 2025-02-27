from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substring = s[6:10].lower()
    letters = [c for c in substring if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes