from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:7].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for r in range(5, len(s) + 1):
        for perm in permutations(s, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes