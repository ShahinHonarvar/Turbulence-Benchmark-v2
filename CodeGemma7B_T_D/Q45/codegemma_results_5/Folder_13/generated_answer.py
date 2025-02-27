from itertools import permutations as perm

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    for p in perm(s[3:10]):
        if is_palindrome(''.join(p).lower()):
            palindromes.add(''.join(p).lower())
    return palindromes