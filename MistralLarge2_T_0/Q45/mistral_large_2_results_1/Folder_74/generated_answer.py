from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c for c in s[1:7] if c.isalpha()]
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm).lower()
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes