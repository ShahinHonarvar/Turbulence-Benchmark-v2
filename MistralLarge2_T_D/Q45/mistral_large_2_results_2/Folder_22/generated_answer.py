from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[5:7] if c.isalpha()]
    letters = ''.join(letters).lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        for length in range(3, len(letters) + 1):
            for perm in permutations(letters, length):
                word = ''.join(perm)
                if is_palindrome(word):
                    palindromes.add(word)
    generate_palindromes(letters)
    return palindromes