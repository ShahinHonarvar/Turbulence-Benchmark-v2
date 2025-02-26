from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:10] if c.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        palindromes = set()
        unique_perms = set(permutations(letters))
        for perm in unique_perms:
            for length in range(5, len(perm) + 1):
                for start in range(len(perm) - length + 1):
                    candidate = ''.join(perm[start:start + length])
                    if is_palindrome(candidate):
                        palindromes.add(candidate)
        return palindromes
    return generate_palindromes(letters)