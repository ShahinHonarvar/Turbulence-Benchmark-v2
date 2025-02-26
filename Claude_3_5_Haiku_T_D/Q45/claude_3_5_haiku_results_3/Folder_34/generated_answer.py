from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:8] if c.isalpha()]
    if len(letters) < 4:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            for j in range(i + 3, len(perm) + 1):
                substring = perm[i:j]
                if len(substring) >= 4:
                    candidate = substring + substring[::-1]
                    if len(candidate) % 2 == 0 and candidate == candidate[::-1]:
                        unique_palindromes.add(candidate)
    return unique_palindromes