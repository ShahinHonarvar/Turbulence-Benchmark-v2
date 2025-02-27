import itertools

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = ''.join([c for c in s[1:7] if c.isalpha()]).lower()
    permutations = set(itertools.permutations(substring, len(substring)))
    palindromes = {p for p in permutations if len(p) >= 6 and is_palindrome(p)}
    return {''.join(p) for p in palindromes}