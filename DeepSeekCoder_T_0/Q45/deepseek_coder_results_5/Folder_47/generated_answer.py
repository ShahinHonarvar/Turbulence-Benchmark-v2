from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[3:8])).lower()
    palindromes = set()
    n = len(letters)
    if n < 5:
        return palindromes
    for perm in permutations(letters, 5):
        if is_palindrome(perm):
            palindromes.add(''.join(perm))
    return palindromes