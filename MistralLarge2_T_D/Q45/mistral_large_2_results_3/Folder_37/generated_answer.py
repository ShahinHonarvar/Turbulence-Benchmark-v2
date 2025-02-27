from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[1:5] if c.isalpha()))
    palindromes = set()
    length = len(letters)

    def is_palindrome(word):
        return word == word[::-1]
    if length < 5:
        return palindromes
    for r in range(5, length + 1):
        for perm in permutations(letters, r):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes