from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    segment = s[5:10].lower()
    letters = [ch for ch in segment if ch.isalpha()]
    palindromes = set()
    for i in range(6, len(letters) + 1):
        for perm in permutations(letters, i):
            joined_perm = ''.join(perm)
            if is_palindrome(joined_perm):
                palindromes.add(joined_perm)
    return palindromes