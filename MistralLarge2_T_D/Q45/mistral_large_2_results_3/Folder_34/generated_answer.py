from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    letters = [c for c in s[5:8] if c.isalpha()]
    all_permutations = set(permutations(letters))
    palindromes = set()
    for perm in all_permutations:
        word = ''.join(perm)
        if len(word) >= 4 and is_palindrome(word):
            palindromes.add(word.lower())
    return palindromes