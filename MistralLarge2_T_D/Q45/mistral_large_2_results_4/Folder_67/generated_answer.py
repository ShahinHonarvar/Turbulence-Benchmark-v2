import itertools

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c for c in s[2:7] if c.isalpha()]
    lowercase_letters = [c.lower() for c in letters]
    permutations = set((''.join(p) for p in itertools.permutations(lowercase_letters, len(lowercase_letters))))
    return {p for p in permutations if is_palindrome(p) and len(p) >= 5}