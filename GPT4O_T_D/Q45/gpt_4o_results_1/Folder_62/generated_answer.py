from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[:9].lower()
    chars = ''.join(filter(str.isalpha, s))
    palindromes = set()
    if len(chars) < 7:
        return palindromes
    for length in range(7, len(chars) + 1):
        for p in set(permutations(chars, length)):
            candidate = ''.join(p)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes