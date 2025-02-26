from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:7] if c.isalpha()]
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            candidate = list(perm)
            if len(candidate) >= 6 and candidate == candidate[::-1]:
                palindromes.add(''.join(candidate))
    return palindromes