from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    substr = s[1:7]
    filtered_chars = [char.lower() for char in substr if char.isalpha()]
    palindromes = set()
    for length in range(3, len(filtered_chars) + 1):
        for perm in permutations(filtered_chars, length):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                palindromes.add(perm_str)
    return palindromes