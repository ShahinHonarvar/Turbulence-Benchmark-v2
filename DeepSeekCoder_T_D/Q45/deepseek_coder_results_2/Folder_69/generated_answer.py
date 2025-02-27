from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[0:4])).lower()
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if len(word) >= 4 and is_palindrome(word):
            palindromes.add(word)
    return palindromes