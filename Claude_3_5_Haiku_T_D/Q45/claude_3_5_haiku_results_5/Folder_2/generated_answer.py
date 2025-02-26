from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:6] if char.isalpha()]

    def generate_palindromes(chars):
        palindromes = set()
        for perm in set(permutations(chars)):
            if len(perm) >= 6:
                for i in range(len(perm) - 5):
                    candidate = perm[i:i + 6]
                    if candidate == candidate[::-1]:
                        palindromes.add(''.join(candidate))
        return palindromes
    return generate_palindromes(letters)