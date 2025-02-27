from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    if len(s) < 8:
        return set()
    substring = s[4:8].lower()
    letters = [char for char in substring if char.isalpha()]
    if len(letters) < 5:
        return set()
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        word = ''.join(perm)
        if len(word) >= 5 and is_palindrome(word):
            palindromes.add(word)
    return palindromes