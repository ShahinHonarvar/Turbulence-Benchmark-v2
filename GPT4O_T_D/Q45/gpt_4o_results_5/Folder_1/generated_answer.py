from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s.lower()
    if len(s) < 8:
        return set()
    letters = [c for c in s[4:8] if c.isalpha()]
    results = set()
    for size in range(5, len(letters) + 1):
        for perm in permutations(letters, size):
            word = ''.join(perm)
            if is_palindrome(word):
                results.add(word)
    return results