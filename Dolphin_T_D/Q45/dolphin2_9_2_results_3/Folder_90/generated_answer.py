import string
    from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        s = s.lower()
        i, j = (0, len(s) - 1)
        while i < j:
            if s[i] != s[j]:
                return False
            i, j = (i + 1, j - 1)
        return True
    s = s[:6]
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(4, len(letters) + 1):
        for p in permutations(letters, i):
            w = ''.join(p)
            if is_palindrome(w):
                palindromes.add(w)
    return palindromes