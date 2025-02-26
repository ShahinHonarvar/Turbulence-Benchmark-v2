from itertools import permutations

def palindromes_between_indices(s):
    s_lower = s.lower()
    substr = s_lower[2:9]
    letters = [char for char in substr if char.isalpha()]

    def generate_palindromes(chars):
        unique_palindromes = set()
        for perm in set(permutations(chars)):
            for length in range(4, len(perm) + 1):
                for start in range(len(perm) - length + 1):
                    candidate = perm[start:start + length]
                    if list(candidate) == list(candidate)[::-1]:
                        unique_palindromes.add(''.join(candidate))
        return unique_palindromes
    return generate_palindromes(letters)