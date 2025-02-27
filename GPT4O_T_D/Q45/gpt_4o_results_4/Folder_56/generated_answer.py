from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    lower_s = s[5:10].lower()
    letters = [c for c in lower_s if c.isalpha()]
    results = set()
    for length in range(5, 6):
        for perm in permutations(letters, length):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                results.add(perm_str)
    return results