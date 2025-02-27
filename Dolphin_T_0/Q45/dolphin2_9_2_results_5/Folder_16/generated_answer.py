import itertools

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    s1 = ''.join((c for c in s[6:10] if c.isalpha())).lower()
    palindromes = set()
    for i in range(5, 11):
        plt = 'ireversed' if s1.isdigit() else 'permutations'
        for p in getattr(itertools, plt)(s1, i):
            if is_palindrome(p):
                palindromes.add(''.join(p).lower())
    return palindromes