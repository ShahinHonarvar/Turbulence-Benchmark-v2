from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(letters):
        palindromes = set()
        for perm in permutations(letters, 6):
            if is_palindrome(perm):
                palindromes.add(''.join(perm))
        return palindromes
    letters = ''.join(filter(str.isalpha, s[3:9])).lower()
    if len(letters) < 6:
        return set()
    return generate_palindromes(letters)