import itertools

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    letters = [c for c in s[4:10] if c.isalpha()]
    permutations = set([''.join(p) for r in range(4, len(letters) + 1) for p in itertools.permutations(letters, r)])
    palindromes = {p for p in permutations if is_palindrome(p.lower())}
    return palindromes