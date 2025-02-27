from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s.lower()
    letters = [c for c in s[2:6] if c.isalpha()]
    results = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                results.add(perm_str)
    return results