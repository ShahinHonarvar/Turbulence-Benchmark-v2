from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[4:8])).lower()
    palindromes = set()
    n = len(letters)
    if n < 5:
        return palindromes
    for perm in permutations(letters, 5):
        word = ''.join(perm)
        if is_palindrome(word):
            palindromes.add(word)
    return palindromes