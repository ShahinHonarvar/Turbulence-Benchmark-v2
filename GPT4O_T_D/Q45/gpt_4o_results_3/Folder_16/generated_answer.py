from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substr = s[6:10].lower()
    letters = [char for char in substr if char.isalpha()]
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for perm in permutations(letters, length):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes