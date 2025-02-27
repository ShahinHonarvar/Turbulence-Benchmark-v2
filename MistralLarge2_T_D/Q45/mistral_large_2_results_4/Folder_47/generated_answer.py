import itertools

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[3:8]
    letters = [c for c in substring if c.isalpha()]
    permutations = set(itertools.permutations(letters, 5))
    palindromes = set()
    for perm in permutations:
        word = ''.join(perm)
        if is_palindrome(word.lower()):
            palindromes.add(word.lower())
    return palindromes