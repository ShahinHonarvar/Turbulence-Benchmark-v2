from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    letters = [c for c in s[1:7] if c.isalpha()]
    palindromes = {''.join(p) for i in range(4, len(letters) + 1) for p in permutations(letters, i) if is_palindrome(p)}
    return palindromes