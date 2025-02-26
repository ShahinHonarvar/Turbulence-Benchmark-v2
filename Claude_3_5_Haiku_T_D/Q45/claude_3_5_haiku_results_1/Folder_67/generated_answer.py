from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:7] if c.isalpha()]
    if len(letters) < 5:
        return set()
    palindromes = set()
    for perm in set(permutations(letters, 5)):
        for arrangement in set(permutations(perm)):
            candidate = ''.join(arrangement)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes