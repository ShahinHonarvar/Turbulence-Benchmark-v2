from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[0:7].lower()))
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        if is_palindrome(perm):
            palindromes.add(''.join(perm))
    return {p for p in palindromes if len(p) >= 7}