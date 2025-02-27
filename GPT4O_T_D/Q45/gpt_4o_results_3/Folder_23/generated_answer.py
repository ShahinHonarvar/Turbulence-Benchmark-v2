from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = ''.join(filter(str.isalpha, s))
    unique_palindromes = set()
    for i in range(4, len(letters) + 1):
        for perm in set(permutations(letters, i)):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                unique_palindromes.add(perm_str)
    return unique_palindromes