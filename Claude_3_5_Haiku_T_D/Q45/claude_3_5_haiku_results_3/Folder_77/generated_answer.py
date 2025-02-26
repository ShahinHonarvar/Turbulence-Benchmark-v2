from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:7].lower()
    letters = [char for char in substring if char.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars):
        palindromes = set()
        for length in range(4, len(chars) + 1):
            for perm in permutations(chars, length):
                for arrangement in set(permutations(perm)):
                    word = ''.join(arrangement)
                    if is_palindrome(word):
                        palindromes.add(word)
        return palindromes
    return generate_palindromes(letters)