from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = ''.join([c.lower() for c in s[2:6] if c.isalpha()])
    if len(substring) < 3:
        return set()
    palindromes = set()
    for length in range(3, len(substring) + 1):
        for perm in permutations(substring, length):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes