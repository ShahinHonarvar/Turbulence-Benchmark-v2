import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[4:8] if c.isalpha()]
    letters = ''.join(letters).lower()

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for p in itertools.permutations(letters, r):
            if is_palindrome(p):
                palindromes.add(''.join(p))
    return palindromes