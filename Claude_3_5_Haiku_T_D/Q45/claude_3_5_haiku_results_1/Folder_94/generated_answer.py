from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[3:5] if char.isalpha()]
    if len(letters) < 3:
        return set()

    def generate_palindromes(letters):
        unique_palindromes = set()
        for perm in set(permutations(letters)):
            for i in range(len(perm)):
                for j in range(i + 2, len(perm) + 1):
                    candidate = perm[i:j] + perm[i:j - 1][::-1]
                    if len(candidate) >= 3:
                        unique_palindromes.add(''.join(candidate))
        return unique_palindromes
    return generate_palindromes(letters)