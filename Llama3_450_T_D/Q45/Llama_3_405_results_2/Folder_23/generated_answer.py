from itertools import permutations

def palindromes_between_indices(s):
    s = ''.join((c for c in s[0:7] if c.isalpha())).lower()
    palindromes = set()
    for r in range(4, len(s) + 1):
        for perm in permutations(s, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes