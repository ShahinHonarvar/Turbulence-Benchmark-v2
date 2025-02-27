import itertools

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = ''.join(sorted([c.lower() for c in s[3:8] if c.isalpha()]))
    palindromes = set()
    for i in range(5, len(s) + 1):
        for p in itertools.permutations(s, i):
            if is_palindrome(''.join(p)):
                palindromes.add(''.join(p))
    return palindromes