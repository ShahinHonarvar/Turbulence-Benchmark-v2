from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[1:7].lower()
    letters_only = ''.join(filter(str.isalpha, s))
    all_palindromes = set()
    for length in range(4, len(letters_only) + 1):
        for perm in permutations(letters_only, length):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                all_palindromes.add(candidate)
    return all_palindromes