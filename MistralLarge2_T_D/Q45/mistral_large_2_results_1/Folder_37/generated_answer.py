from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    chars = [c for c in s[1:5] if c.isalpha()]
    palindromes = set()
    for length in range(5, len(chars) + 1):
        for perm in permutations(chars, length):
            word = ''.join(perm).lower()
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes