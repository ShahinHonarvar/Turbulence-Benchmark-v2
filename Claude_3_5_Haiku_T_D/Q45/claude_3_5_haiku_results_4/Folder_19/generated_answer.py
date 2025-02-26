from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        palindromes = set()
        for length in range(7, len(letters) + 1):
            for perm in set(permutations(letters, length)):
                for arrangement in set(permutations(perm)):
                    word = ''.join(arrangement).lower()
                    if is_palindrome(word):
                        palindromes.add(word)
        return palindromes
    if len(s) < 8:
        return set()
    letters = [char for char in s[1:8] if char.isalpha()]
    return generate_palindromes(letters)