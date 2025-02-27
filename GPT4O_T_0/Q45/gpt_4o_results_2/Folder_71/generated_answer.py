from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    substring = ''.join([c for c in s[1:4] if c.isalpha()])
    palindromes = set()
    for length in range(4, len(substring) + 1):
        for perm in permutations(substring, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes