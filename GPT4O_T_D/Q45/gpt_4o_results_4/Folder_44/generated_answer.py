from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    subset = s[2:8].lower()
    letters = [char for char in subset if char.isalpha()]
    unique_palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            permuted_str = ''.join(perm)
            if is_palindrome(permuted_str):
                unique_palindromes.add(permuted_str)
    return unique_palindromes