from itertools import permutations

def palindromes_between_indices(s):
    substring = ''.join((c for c in s[4:10] if c.isalpha())).lower()
    palindromes = set()
    for length in range(4, len(substring) + 1):
        for perm in permutations(substring, length):
            palindrome = ''.join(perm)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes