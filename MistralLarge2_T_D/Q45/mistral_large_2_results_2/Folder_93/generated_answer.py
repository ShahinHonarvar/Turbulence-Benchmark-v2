import itertools

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    chars = [c.lower() for c in s[2:8] if c.isalpha()]
    permutations = set((''.join(p) for r in range(6, len(chars) + 1) for p in itertools.permutations(chars, r)))
    palindromes = {p for p in permutations if is_palindrome(p)}
    return palindromes