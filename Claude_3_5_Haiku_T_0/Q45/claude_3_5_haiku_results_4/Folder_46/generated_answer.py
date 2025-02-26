from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:10] if c.isalpha()]
    if len(letters) < 6:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters, 6)):
        for i in range(3):
            candidate = perm[0:3] + perm[3::-1]
            if len(set(candidate)) == 6:
                unique_palindromes.add(''.join(candidate))
    return unique_palindromes