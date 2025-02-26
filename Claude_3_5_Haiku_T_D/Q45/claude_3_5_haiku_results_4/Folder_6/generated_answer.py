from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        result = set()
        perms = set((''.join(p).lower() for p in permutations(letters)))
        for perm in perms:
            for length in range(4, len(perm) + 1):
                for start in range(len(perm) - length + 1):
                    substr = perm[start:start + length]
                    if is_palindrome(substr):
                        result.add(substr)
        return result
    letters = [char for char in s[:8].lower() if char.isalpha()]
    return generate_palindromes(letters)