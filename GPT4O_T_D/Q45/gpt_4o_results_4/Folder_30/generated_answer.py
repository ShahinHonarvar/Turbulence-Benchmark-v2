from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[0:5].lower()
    letter_list = [char for char in s if char.isalpha()]
    unique_palindromes = set()
    for length in range(4, len(letter_list) + 1):
        for perm in set(permutations(letter_list, length)):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                unique_palindromes.add(perm_str)
    return unique_palindromes