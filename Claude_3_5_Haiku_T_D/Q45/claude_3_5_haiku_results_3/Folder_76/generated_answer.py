from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    letters = [char.lower() for char in s[1:5] if char.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            candidate = ''.join(perm[i:] + perm[:i])
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return {p for p in palindromes if len(p) >= 4}