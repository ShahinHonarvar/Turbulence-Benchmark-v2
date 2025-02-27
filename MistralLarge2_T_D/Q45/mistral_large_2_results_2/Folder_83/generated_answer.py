from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    subset = s[2:10]
    letters = [c for c in subset if c.isalpha()]
    if len(letters) < 7:
        return set()
    palindromes = set()
    for r in range(7, len(letters) + 1):
        for p in permutations(letters, r):
            word = ''.join(p).lower()
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes