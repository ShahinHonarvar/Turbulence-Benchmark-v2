from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[:7].lower()
    english_letters = ''.join(filter(str.isalpha, s))
    result = set()
    for perm in permutations(english_letters):
        perm_str = ''.join(perm)
        if len(perm_str) >= 6 and is_palindrome(perm_str):
            result.add(perm_str)
    return result