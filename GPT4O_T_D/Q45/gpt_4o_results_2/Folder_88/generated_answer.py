from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    substring = s[3:8].lower()
    valid_chars = ''.join(filter(str.isalpha, substring))
    palindromes = set()
    for length in range(6, len(valid_chars) + 1):
        for p in set(permutations(valid_chars, length)):
            candidate = ''.join(p)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes