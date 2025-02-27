from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s if c.isalpha()]
    letters = letters[3:7]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for perm in permutations(letters):
        candidate = ''.join(perm)
        if len(candidate) >= 3 and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes