from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 7:
        return set()
    substring = s[5:7]
    letters = [c.lower() for c in substring if c.isalpha()]
    if len(letters) < 3:
        return set()

    def generate_palindromes(chars):
        palindromes = set()
        unique_perms = set(permutations(chars))
        for perm in unique_perms:
            for i in range(len(perm)):
                for j in range(i + 3, len(perm) + 1):
                    candidate = list(perm[i:j])
                    if len(candidate) >= 3:
                        pal = candidate + candidate[-2::-1]
                        palindromes.add(''.join(pal))
        return palindromes
    return generate_palindromes(letters)