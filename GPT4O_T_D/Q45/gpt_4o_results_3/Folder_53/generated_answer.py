from itertools import permutations

def palindromes_between_indices(s):
    substr = s[4:9].lower()
    letters_only = ''.join(filter(str.isalpha, substr))
    palindromes = set()
    if len(letters_only) == 0:
        return palindromes
    for length in range(6, len(letters_only) + 1):
        for perm in permutations(letters_only, length):
            if is_palindrome(''.join(perm)):
                palindromes.add(''.join(perm))
    return palindromes

def is_palindrome(s):
    return s == s[::-1]