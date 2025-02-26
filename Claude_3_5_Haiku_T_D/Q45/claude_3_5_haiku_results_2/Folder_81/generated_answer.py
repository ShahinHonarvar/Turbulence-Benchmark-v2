from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars):
        result = set()
        unique_perms = set((''.join(p).lower() for p in permutations(chars)))
        for perm in unique_perms:
            for length in range(3, len(perm) + 1):
                for start in range(len(perm) - length + 1):
                    substr = perm[start:start + length]
                    if is_palindrome(substr):
                        result.add(substr)
        return result
    letters = ''.join((char for char in s[:7] if char.isalpha()))
    return generate_palindromes(letters)