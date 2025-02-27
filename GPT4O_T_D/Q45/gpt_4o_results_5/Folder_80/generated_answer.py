from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[3:9].lower()
    valid_chars = [char for char in s if char.isalpha()]
    palindromes = set()
    for length in range(7, len(valid_chars) + 1):
        for perm in set(permutations(valid_chars, length)):
            if is_palindrome(perm):
                palindromes.add(''.join(perm))
    return palindromes