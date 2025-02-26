from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:5] if char.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            candidate = perm[i:] + perm[:i]
            if len(candidate) >= 3 and candidate == candidate[::-1]:
                palindromes.add(''.join(candidate))
    return palindromes