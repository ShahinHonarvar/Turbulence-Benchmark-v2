from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[2:10]
    chars = [char.lower() for char in s if char.isalpha()]
    possible_palindromes = set()
    for perm in permutations(chars):
        candidate = ''.join(perm)
        if len(candidate) >= 6 and is_palindrome(candidate):
            possible_palindromes.add(candidate)
    return possible_palindromes