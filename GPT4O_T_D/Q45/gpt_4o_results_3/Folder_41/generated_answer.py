from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    chars = [c.lower() for c in s[2:4] if c.isalpha()]
    palindromes = set()
    for length in range(3, len(chars) + 1):
        for perm in permutations(chars, length):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes