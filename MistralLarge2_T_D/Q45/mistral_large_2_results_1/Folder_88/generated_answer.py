from itertools import permutations

def palindromes_between_indices(s):
    substring = ''.join((c for c in s[3:8] if c.isalpha())).lower()
    palindromes = set()
    for length in range(6, len(substring) + 1):
        for p in permutations(substring, length):
            palindrome = ''.join(p)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes