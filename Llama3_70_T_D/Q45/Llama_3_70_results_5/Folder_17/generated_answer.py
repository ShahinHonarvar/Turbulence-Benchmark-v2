from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:7].lower()
    palindromes = set()
    for r in range(4, len(s) + 1):
        for perm in permutations(s, r):
            if perm == perm[::-1]:
                palindrome = ''.join(perm)
                palindromes.add(palindrome)
    return palindromes