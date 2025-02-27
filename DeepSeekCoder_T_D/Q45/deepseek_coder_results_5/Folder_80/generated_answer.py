from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[3:9])).lower()
    palindromes = set()
    n = len(letters)
    if n < 7:
        return palindromes
    for perm in permutations(letters, 7):
        if is_palindrome(perm):
            palindromes.add(''.join(perm))
    for perm in permutations(letters, 8):
        if is_palindrome(perm):
            palindromes.add(''.join(perm))
    for perm in permutations(letters, 9):
        if is_palindrome(perm):
            palindromes.add(''.join(perm))
    return palindromes