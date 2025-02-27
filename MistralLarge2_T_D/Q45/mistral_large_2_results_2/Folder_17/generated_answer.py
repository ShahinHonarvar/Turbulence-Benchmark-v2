from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    chars = [c for c in s[2:7] if c.isalpha()]
    if len(chars) < 4:
        return set()
    chars = [c.lower() for c in chars]
    perms = set((''.join(p) for p in permutations(chars, len(chars))))
    palindromes = {p for p in perms if is_palindrome(p) and len(p) >= 4}
    return palindromes