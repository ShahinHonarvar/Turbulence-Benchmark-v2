from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:6] if c.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        unique_palindromes = set()
        for length in range(4, len(letters) + 1):
            for perm in set(permutations(letters, length)):
                for p in set(permutations(perm)):
                    word = ''.join(p)
                    if len(word) >= 4 and is_palindrome(word):
                        unique_palindromes.add(word)
        return unique_palindromes
    return generate_palindromes(letters)