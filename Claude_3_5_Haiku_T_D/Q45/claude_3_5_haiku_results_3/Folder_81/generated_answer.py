from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        unique_palindromes = set()
        for length in range(3, len(letters) + 1):
            for perm in set(permutations(letters, length)):
                for arrangement in set(permutations(perm)):
                    candidate = ''.join(arrangement).lower()
                    if is_palindrome(candidate):
                        unique_palindromes.add(candidate)
        return unique_palindromes
    extracted_letters = [char.lower() for char in s[:7] if char.isalpha()]
    return generate_palindromes(extracted_letters)