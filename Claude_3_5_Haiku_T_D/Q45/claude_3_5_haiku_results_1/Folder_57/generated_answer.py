from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:6] if c.isalpha()]
    if len(letters) < 5:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters)):
        for length in range(5, len(perm) + 1):
            for start in range(len(perm) - length + 1):
                candidate = perm[start:start + length]
                candidate_str = ''.join(candidate)
                if candidate_str == candidate_str[::-1]:
                    unique_palindromes.add(candidate_str)
    return unique_palindromes