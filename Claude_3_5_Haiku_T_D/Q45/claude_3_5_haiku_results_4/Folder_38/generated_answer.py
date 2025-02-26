from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    letter_range = s[3:9]
    letters = [char for char in letter_range if char.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        unique_palindromes = set()
        for length in range(5, len(letters) + 1):
            for perm in set(permutations(letters, length)):
                for arrangement in set(permutations(perm)):
                    word = ''.join(arrangement)
                    if is_palindrome(word):
                        unique_palindromes.add(word)
        return unique_palindromes
    return generate_palindromes(letters)