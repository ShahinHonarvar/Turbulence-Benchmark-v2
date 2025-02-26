from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:6] if c.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, min_length=3):
        palindromes = set()
        for length in range(min_length, len(chars) + 1):
            for perm in permutations(chars, length):
                word = ''.join(perm)
                if is_palindrome(word):
                    palindromes.add(word)
        return palindromes
    return generate_palindromes(letters)