from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[0:6].lower()))
    palindromes = set()
    for perm in permutations(letters, 5):
        word = ''.join(perm)
        if is_palindrome(word):
            palindromes.add(word)
    return palindromes