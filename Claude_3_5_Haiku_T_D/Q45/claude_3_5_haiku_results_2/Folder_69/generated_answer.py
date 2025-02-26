from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[:4] if char.isalpha()]

    def generate_palindromes(chars):

        def is_palindrome(word):
            return word == word[::-1]
        unique_palindromes = set()
        for perm in set(permutations(chars)):
            for length in range(4, len(perm) + 1):
                for start in range(len(perm) - length + 1):
                    subset = perm[start:start + length]
                    word = ''.join(subset)
                    if is_palindrome(word):
                        unique_palindromes.add(word)
        return {p for p in unique_palindromes if len(p) >= 4}
    return generate_palindromes(letters)