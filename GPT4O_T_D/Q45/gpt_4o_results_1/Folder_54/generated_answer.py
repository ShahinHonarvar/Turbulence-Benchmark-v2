from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substr = s[4:10].lower()
    filtered_letters = ''.join(filter(str.isalpha, substr))
    all_perms = set((''.join(p) for i in range(4, len(filtered_letters) + 1) for p in permutations(filtered_letters, i)))
    palindromes = {p for p in all_perms if is_palindrome(p)}
    return palindromes