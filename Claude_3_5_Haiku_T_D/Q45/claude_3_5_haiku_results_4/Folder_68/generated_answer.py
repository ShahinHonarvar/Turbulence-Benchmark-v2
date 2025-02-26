from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        unique_palindromes = set()
        for perm in set(permutations(letters)):
            for length in range(4, len(perm) + 1):
                for start in range(len(perm) - length + 1):
                    subset = perm[start:start + length]
                    for arrangement in set(permutations(subset)):
                        word = ''.join(arrangement).lower()
                        if is_palindrome(word):
                            unique_palindromes.add(word)
        return unique_palindromes
    letters = [char.lower() for char in s[1:9] if char.isalpha()]
    return generate_palindromes(letters)