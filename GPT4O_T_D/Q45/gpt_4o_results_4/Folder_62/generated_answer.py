from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    substr = s[0:9].lower()
    letters = [c for c in substr if c.isalpha()]
    palindromes = set()
    for length in range(7, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes