from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[4:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if len(word) >= 5 and is_palindrome(word):
            palindromes.add(word)
    return palindromes