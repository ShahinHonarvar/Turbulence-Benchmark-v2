from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[2:4] if c.isalpha()))
    if len(letters) < 3:
        return set()

    def generate_palindromes(chars):
        palindromes = set()
        unique_perms = set(permutations(chars))
        for perm in unique_perms:
            for length in range(3, len(perm) + 1):
                for i in range(len(perm) - length + 1):
                    substr = perm[i:i + length]
                    if substr == substr[::-1]:
                        palindromes.add(''.join(substr))
        return palindromes
    return generate_palindromes(letters)