from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    s = s[1:10].lower()
    filtered_chars = [char for char in s if char.isalpha()]
    palindrome_set = set()
    for length in range(7, len(filtered_chars) + 1):
        for perm in permutations(filtered_chars, length):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                palindrome_set.add(perm_str)
    return palindrome_set