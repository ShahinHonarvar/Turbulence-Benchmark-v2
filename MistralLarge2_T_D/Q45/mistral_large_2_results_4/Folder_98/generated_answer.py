from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    letters = ''.join(filter(str.isalpha, s[3:6])).lower()
    all_permutations = set((''.join(p) for i in range(4, len(letters) + 1) for p in permutations(letters, i)))
    palindromes = {p for p in all_permutations if is_palindrome(p)}
    return palindromes