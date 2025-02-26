from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[6:9] if char.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars):
        unique_palindromes = set()
        for perm in set(permutations(chars)):
            for length in range(3, len(perm) + 1):
                for start in range(len(perm) - length + 1):
                    candidate = perm[start:start + length]
                    word = ''.join(candidate)
                    if is_palindrome(word):
                        unique_palindromes.add(word)
        return unique_palindromes
    return generate_palindromes(letters)