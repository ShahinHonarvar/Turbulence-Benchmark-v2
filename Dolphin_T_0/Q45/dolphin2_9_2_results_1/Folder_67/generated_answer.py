from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        s = s.lower()
        return s == s[::-1]
    s = s[2:7]
    perms = set()
    for i in range(5, len(s) + 1):
        for perm in permutations(s, i):
            if is_palindrome(''.join(perm)):
                perms.add(''.join(perm))
    return perms