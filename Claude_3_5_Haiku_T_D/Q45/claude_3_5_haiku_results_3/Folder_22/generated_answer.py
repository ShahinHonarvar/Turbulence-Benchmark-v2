from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:7] if c.isalpha()]
    if len(letters) < 3:
        return set()

    def create_palindromes(chars):
        palindromes = set()
        for perm in set(permutations(chars)):
            for length in range(3, len(perm) + 1):
                for start in range(len(perm) - length + 1):
                    candidate = perm[start:start + length]
                    if candidate == candidate[::-1]:
                        palindromes.add(''.join(candidate))
        return palindromes
    return create_palindromes(letters)