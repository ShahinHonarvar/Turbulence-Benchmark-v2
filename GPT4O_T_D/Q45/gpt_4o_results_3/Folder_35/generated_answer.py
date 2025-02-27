from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    substr = s[2:5].lower()
    english_letters = ''.join(filter(str.isalpha, substr))
    if len(english_letters) < 4:
        return set()
    potential_palindromes = set()
    for length in range(4, len(english_letters) + 1):
        for perm in set(permutations(english_letters, length)):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                potential_palindromes.add(perm_str)
    return potential_palindromes