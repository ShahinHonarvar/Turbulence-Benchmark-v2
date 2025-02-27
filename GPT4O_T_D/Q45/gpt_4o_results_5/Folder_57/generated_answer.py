from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    subsequence = ''.join([char.lower() for char in s[2:6] if char.isalpha()])
    if len(subsequence) < 5:
        return set()
    palindromes = set()
    for perm in permutations(subsequence):
        perm_str = ''.join(perm)
        if is_palindrome(perm_str) and len(perm_str) >= 5:
            palindromes.add(perm_str)
    return palindromes