from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[5:10].lower()))
    palindromes = set()
    n = len(letters)
    if n < 6:
        return palindromes
    for perm in permutations(letters, 6):
        word = ''.join(perm)
        if is_palindrome(word):
            palindromes.add(word)
    return palindromes