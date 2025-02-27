from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    s = s[:5].lower()
    alphas = [ch for ch in s if ch.isalpha()]
    result = set()
    for length in range(3, len(alphas) + 1):
        for perm in permutations(alphas, length):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                result.add(perm_str)
    return result