from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[0:3] if char.isalpha()]
    unique_palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for candidate in [perm, perm[::-1]]:
                candidate_str = ''.join(candidate)
                if candidate_str == candidate_str[::-1]:
                    unique_palindromes.add(candidate_str)
    return unique_palindromes