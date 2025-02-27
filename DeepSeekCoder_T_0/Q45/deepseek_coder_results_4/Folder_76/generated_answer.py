from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[1:5])).lower()
    palindromes = set()
    n = len(letters)
    if n < 4:
        return palindromes
    for perm in permutations(letters, 4):
        word = ''.join(perm)
        if is_palindrome(word):
            palindromes.add(word)
    return palindromes