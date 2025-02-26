from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars):
        unique_palindromes = set()
        for perm in set(permutations(chars)):
            for i in range(len(perm)):
                for j in range(i + 4, len(perm) + 1):
                    current = perm[i:j]
                    if len(current) >= 4:
                        word = ''.join(current).lower()
                        if is_palindrome(word):
                            unique_palindromes.add(word)
        return unique_palindromes
    letters = [char.lower() for char in s[1:9] if char.isalpha()]
    return generate_palindromes(letters)