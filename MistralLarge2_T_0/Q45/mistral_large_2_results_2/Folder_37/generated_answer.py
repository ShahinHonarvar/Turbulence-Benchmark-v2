from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c for c in s[1:5] if c.isalpha()]
    if len(letters) < 5:
        return set()
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm).lower()
        if len(word) >= 5 and is_palindrome(word):
            palindromes.add(word)
    return palindromes