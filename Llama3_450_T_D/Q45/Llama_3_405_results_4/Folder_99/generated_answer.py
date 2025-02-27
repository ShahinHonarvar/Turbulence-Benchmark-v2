import itertools

def palindromes_between_indices(s):

    def is_palindrome(t):
        return t == t[::-1]
    letters = [c.lower() for c in s[4:9] if c.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for p in itertools.permutations(letters, r):
            t = ''.join(p)
            if is_palindrome(t):
                palindromes.add(t)
    return palindromes