from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        palindromes = set()
        unique_perms = set((''.join(p).lower() for p in permutations(letters)))
        for perm in unique_perms:
            for length in range(6, len(perm) + 1):
                for start in range(len(perm) - length + 1):
                    substr = perm[start:start + length]
                    if is_palindrome(substr):
                        palindromes.add(substr)
        return palindromes
    letters = ''.join((c for c in s[:6] if c.isalpha()))
    return generate_palindromes(letters)