from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[8:10] if char.isalpha()]
    if len(letters) < 3:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            for j in range(i + 2, len(perm) + 1):
                candidate = perm[i:j] + perm[i:j][::-1]
                if len(candidate) >= 6 and candidate == candidate[::-1]:
                    unique_palindromes.add(candidate)
    return unique_palindromes