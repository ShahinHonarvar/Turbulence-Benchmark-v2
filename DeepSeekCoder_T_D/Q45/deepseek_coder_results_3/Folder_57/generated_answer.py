from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[2:6].lower()))
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        if len(perm) >= 5 and is_palindrome(''.join(perm)):
            palindromes.add(''.join(perm))
    return palindromes