from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for p in permutations(s[4:5], len(s[4:5])):
        word = ''.join(p).lower()
        if len(word) >= 3 and is_palindrome(word):
            palindromes.add(word)
    return palindromes