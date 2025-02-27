from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    range_chars = [c.lower() for c in s[1:6] if c.isalpha()]
    palindromes_set = set()
    for length in range(5, len(range_chars) + 1):
        for perm in permutations(range_chars, length):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                palindromes_set.add(candidate)
    return palindromes_set