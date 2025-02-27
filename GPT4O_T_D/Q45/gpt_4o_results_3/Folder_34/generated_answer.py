from itertools import permutations

def palindromes_between_indices(s):
    substring = s[5:8].lower()
    letters = [c for c in substring if c.isalpha()]
    if len(letters) < 4:
        return set()

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        word = ''.join(perm)
        if len(word) >= 4 and is_palindrome(word):
            palindromes.add(word)
    return palindromes