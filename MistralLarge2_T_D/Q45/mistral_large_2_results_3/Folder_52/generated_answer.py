from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c for c in s[:8] if c.isalpha()]
    perm_set = set()
    for length in range(6, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm).lower()
            if is_palindrome(word):
                perm_set.add(word)
    return perm_set