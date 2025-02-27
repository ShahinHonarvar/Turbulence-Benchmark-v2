from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    subset = s[7:10].lower()
    letters = [c for c in subset if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if is_palindrome(word) and len(word) >= 3:
            palindromes.add(word)
    return palindromes