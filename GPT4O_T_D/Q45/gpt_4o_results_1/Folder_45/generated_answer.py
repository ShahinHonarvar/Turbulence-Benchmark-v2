from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    substring = s[5:10].lower()
    filtered_chars = [c for c in substring if c.isalpha()]
    if len(filtered_chars) < 4:
        return set()
    possible_palindromes = set()
    for i in range(4, len(filtered_chars) + 1):
        for perm in permutations(filtered_chars, i):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                possible_palindromes.add(perm_str)
    return possible_palindromes