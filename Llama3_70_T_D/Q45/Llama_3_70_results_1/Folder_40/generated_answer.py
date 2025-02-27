from itertools import permutations

def palindromes_between_indices(s):
    palindrome_set = set()
    s = s[4:10].lower()
    for r in range(7, len(s) + 1):
        for p in permutations(s, r):
            if p == p[::-1]:
                palindrome_set.add(''.join(p))
    return palindrome_set