from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    middle_chars = s[1:7]
    char_set = [ch.lower() for ch in middle_chars if ch.isalpha()]
    palindromes = set()
    for i in range(4, len(char_set) + 1):
        for perm in set(permutations(char_set, i)):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                palindromes.add(perm_str)
    return palindromes