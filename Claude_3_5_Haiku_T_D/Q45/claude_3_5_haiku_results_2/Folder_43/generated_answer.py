from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    substr = s[2:6].lower()
    letters = [char for char in substr if char.isalpha()]
    if len(letters) < 4:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            candidate = ''.join(perm[i:] + perm[:i])
            if len(candidate) >= 4 and candidate == candidate[::-1]:
                unique_palindromes.add(candidate)
    return unique_palindromes