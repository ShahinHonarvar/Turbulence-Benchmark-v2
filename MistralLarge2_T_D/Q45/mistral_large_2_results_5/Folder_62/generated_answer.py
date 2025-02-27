from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = ''.join(filter(str.isalpha, s[:9])).lower()
    possible_palindromes = {''.join(p) for p in permutations(substring) if len(p) >= 7 and is_palindrome(p)}
    return {p for p in possible_palindromes if len(p) >= 7}