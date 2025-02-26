from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:9] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            candidate = list(perm[i:] + perm[:i])
            if len(candidate) >= 3 and candidate == candidate[::-1]:
                palindromes.add(''.join(candidate))
    return palindromes