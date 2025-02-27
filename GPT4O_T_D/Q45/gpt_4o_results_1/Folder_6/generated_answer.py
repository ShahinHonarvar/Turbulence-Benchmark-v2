from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[:8].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            potential_palindrome = ''.join(perm)
            if is_palindrome(potential_palindrome):
                palindromes.add(potential_palindrome)
    return palindromes