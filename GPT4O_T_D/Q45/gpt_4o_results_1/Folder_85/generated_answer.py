from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[2:9]
    s = ''.join([char.lower() for char in s if char.isalpha()])
    palindromes = set()
    if len(s) < 1:
        return set()
    for perm_length in range(7, len(s) + 1):
        for perm in permutations(s, perm_length):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes