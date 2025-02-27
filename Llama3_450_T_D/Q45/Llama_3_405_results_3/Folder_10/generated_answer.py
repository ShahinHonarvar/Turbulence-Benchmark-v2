from itertools import permutations

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[:6].lower()))
    palindromes = set()
    for r in range(3, len(s) + 1):
        for perm in permutations(s, r):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes