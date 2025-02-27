from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    max_index_range = 7
    unique_palindromes = set()
    filtered_chars = [char.lower() for char in s[0:max_index_range] if char.isalpha()]
    if len(filtered_chars) < max_index_range:
        return unique_palindromes
    for length in range(7, len(filtered_chars) + 1):
        for perm in permutations(filtered_chars, length):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                unique_palindromes.add(candidate)
    return unique_palindromes