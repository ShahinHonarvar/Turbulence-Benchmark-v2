from itertools import permutations

def palindromes_between_indices(s):
    substr = ''.join((c for c in s[0:8] if c.isalpha())).lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for length in range(4, len(substr) + 1):
        for perm in permutations(substr, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes