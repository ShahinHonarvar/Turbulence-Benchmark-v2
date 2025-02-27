from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[1:7].lower()
    english_letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(7, len(english_letters) + 1):
        perm = permutations(english_letters, i)
        for p in perm:
            candidate = ''.join(p)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return {p for p in palindromes if len(p) >= 7}