import itertools

def palindromes_between_indices(s):
    s = s[1:9]
    s = ''.join((ch.lower() for ch in s if ch.isalpha()))

    def is_palindrome(palindrome):
        return palindrome == palindrome[::-1]
    perms = [itertools.permutations(s, r) for r in range(7, len(s) + 1)]
    perms = itertools.chain(*perms)
    string_perms = [''.join(perm) for perm in perms]
    palindromes = set((perm for perm in string_perms if is_palindrome(perm)))
    return palindromes