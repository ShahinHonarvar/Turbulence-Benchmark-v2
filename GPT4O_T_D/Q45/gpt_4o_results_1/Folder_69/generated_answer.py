from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    limited_range = s[:4].lower()
    char_list = [c for c in limited_range if c.isalpha()]
    unique_palindromes = set()
    for l in range(4, len(char_list) + 1):
        for p in permutations(char_list, l):
            candidate = ''.join(p)
            if is_palindrome(candidate):
                unique_palindromes.add(candidate)
    return unique_palindromes