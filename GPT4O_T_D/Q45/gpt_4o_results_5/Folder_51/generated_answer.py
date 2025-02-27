from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    substring = s[3:6].lower()
    only_letters = ''.join([c for c in substring if c.isalpha()])
    if len(only_letters) < 3:
        return set()

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for perm in permutations(only_letters):
        w = ''.join(perm)
        if len(w) >= 3 and is_palindrome(w):
            palindromes.add(w)
    return palindromes