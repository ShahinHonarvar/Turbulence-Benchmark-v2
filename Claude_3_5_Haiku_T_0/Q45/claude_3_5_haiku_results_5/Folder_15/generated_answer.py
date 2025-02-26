from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 3:
        return set()
    letters = [c.lower() for c in s[1:3] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for arrangement in set(permutations(perm)):
                candidate = ''.join(arrangement)
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes