from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:9] if c.isalpha()]
    palindromes = set()
    for length in range(7, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            if is_palindrome(perm):
                palindromes.add(''.join(perm))
    return palindromes

def is_palindrome(chars):
    return list(chars) == list(chars)[::-1]