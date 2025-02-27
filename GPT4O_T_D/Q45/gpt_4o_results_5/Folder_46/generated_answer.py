from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[4:10].lower()
    chars = [c for c in s if c.isalpha()]
    result = set()
    for length in range(6, len(chars) + 1):
        for perm in permutations(chars, length):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                result.add(perm_str)
    return result