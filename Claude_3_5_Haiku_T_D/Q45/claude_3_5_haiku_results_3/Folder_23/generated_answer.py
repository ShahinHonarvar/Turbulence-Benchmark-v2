from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        unique_palindromes = set()
        for length in range(4, len(letters) + 1):
            for perm in set(permutations(letters, length)):
                for arrangement in set(permutations(perm)):
                    word = ''.join(arrangement).lower()
                    if is_palindrome(word):
                        unique_palindromes.add(word)
        return unique_palindromes
    letters = [char.lower() for char in s[:7] if char.isalpha()]
    return generate_palindromes(letters)