from itertools import permutations

def palindromes_between_indices(s):
    substr = s[2:7].lower()
    letters = [c for c in substr if c.isalpha()]
    unique_palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            if perm[:len(perm) // 2] == tuple(reversed(perm[len(perm) // 2:])):
                unique_palindromes.add(''.join(perm))
    return unique_palindromes