from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(c):
        return c == c[::-1]
    s = s[5:10].lower()
    s = ''.join(filter(str.isalpha, s))
    result = set()
    for perm in permutations(s):
        perm = ''.join(perm)
        if len(perm) >= 6 and is_palindrome(perm):
            result.add(perm)
    return result