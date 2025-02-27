import re
    from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = re.findall('[A-Za-z]', s[4:6])
    perms = set((''.join(p).lower() for r in range(3, len(letters) + 1) for p in permutations(letters, r)))
    palindromes = {word for word in perms if is_palindrome(word)}
    return palindromes