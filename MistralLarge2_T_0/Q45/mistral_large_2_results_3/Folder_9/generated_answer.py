from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c for c in s[:7] if c.isalpha()]
    if len(letters) < 7:
        return set()
    palindromes = set()
    for perm in permutations(letters, 7):
        word = ''.join(perm).lower()
        if is_palindrome(word):
            palindromes.add(word)
    return palindromes