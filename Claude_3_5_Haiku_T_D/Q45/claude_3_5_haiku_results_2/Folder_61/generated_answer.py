from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[:8] if char.isalpha()]
    palindromes = set()
    if len(letters) < 7:
        return palindromes
    for perm in set(permutations(letters, 7)):
        for arrangement in [perm, perm[::-1]]:
            candidate = ''.join(arrangement)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes