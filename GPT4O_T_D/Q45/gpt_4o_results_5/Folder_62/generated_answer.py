from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[:9]
    s = ''.join(filter(str.isalpha, s.lower()))
    result = set()
    for length in range(7, len(s) + 1):
        for perm in permutations(s, length):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                result.add(candidate)
    return result