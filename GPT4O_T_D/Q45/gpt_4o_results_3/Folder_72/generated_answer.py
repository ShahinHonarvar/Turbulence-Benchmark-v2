from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    letters = ''.join([c for c in s[1:8] if c.isalpha()])
    palindromes = set()
    if len(letters) < 6:
        return palindromes
    for perm in permutations(letters):
        perm_str = ''.join(perm)
        for i in range(6, len(perm_str) + 1):
            if is_palindrome(perm_str[:i]):
                palindromes.add(perm_str[:i])
    return palindromes