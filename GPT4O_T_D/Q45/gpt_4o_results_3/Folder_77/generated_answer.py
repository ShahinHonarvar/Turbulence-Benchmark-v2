from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    subset = s[4:7]
    letters = [c.lower() for c in subset if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes