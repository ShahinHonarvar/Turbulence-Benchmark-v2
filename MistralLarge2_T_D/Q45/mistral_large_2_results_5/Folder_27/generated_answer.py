from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars, length):
        palindromes = set()
        for perm in permutations(chars, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word.lower())
        return palindromes
    substring = s[2:9]
    english_letters = [c for c in substring if c.isalpha()]
    palindromes = set()
    for length in range(6, len(english_letters) + 1):
        palindromes.update(generate_palindromes(english_letters, length))
    return palindromes