from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    substring = ''.join(filter(str.isalpha, s[1:9])).lower()
    palindromes = {''.join(p) for i in range(6, len(substring) + 1) for p in permutations(substring, i) if is_palindrome(''.join(p))}
    return {p for p in palindromes if len(p) >= 6}