from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s.lower()
    substring = s[3:10]
    letters = [c for c in substring if c.isalpha()]
    palindromes = set()
    for i in range(5, len(letters) + 1):
        perm = set(permutations(letters, i))
        for p in perm:
            word = ''.join(p)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes