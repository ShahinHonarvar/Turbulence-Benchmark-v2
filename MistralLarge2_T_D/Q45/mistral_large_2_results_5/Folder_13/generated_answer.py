from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c for c in s[3:10] if c.isalpha()]
    n = len(letters)
    result = set()
    for length in range(5, n + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm).lower()
            if is_palindrome(word):
                result.add(word)
    return result