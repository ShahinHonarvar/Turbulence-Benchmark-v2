from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        unique_palindromes = set()
        for perm in set(permutations(letters)):
            word = ''.join(perm).lower()
            for i in range(len(word)):
                for j in range(i + 5, len(word) + 1):
                    subset = word[i:j]
                    if is_palindrome(subset) and len(subset) >= 6:
                        unique_palindromes.add(subset)
        return unique_palindromes
    english_letters = [c.lower() for c in s[:7] if c.isalpha()]
    return generate_palindromes(english_letters)