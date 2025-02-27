from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[2:10].lower()
    letters = [char for char in s if char.isalpha()]
    result = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            if is_palindrome(perm):
                result.add(''.join(perm))
    return result