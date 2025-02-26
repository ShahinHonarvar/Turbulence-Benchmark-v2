from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        palindromes = set()
        for length in range(3, len(letters) + 1):
            for perm in set(permutations(letters, length)):
                for arrangement in set(permutations(perm)):
                    word = ''.join(arrangement).lower()
                    if is_palindrome(word):
                        palindromes.add(word)
        return palindromes
    letters = [char.lower() for char in s[2:8] if char.isalpha()]
    return generate_palindromes(letters)