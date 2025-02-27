from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(string):
    substring = string[2:10].lower()
    letters = [c for c in substring if c.isalpha()]
    result = set()
    for p in permutations(letters):
        candidate = ''.join(p)
        for i in range(4, len(candidate) + 1):
            if is_palindrome(candidate[:i]):
                result.add(candidate[:i])
    return result