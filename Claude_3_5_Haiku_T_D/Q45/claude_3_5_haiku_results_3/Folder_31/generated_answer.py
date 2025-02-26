from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:9] if c.isalpha()]
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes