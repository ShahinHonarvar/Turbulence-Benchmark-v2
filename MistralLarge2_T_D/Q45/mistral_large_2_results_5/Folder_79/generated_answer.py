from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = ''.join(filter(str.isalpha, s[1:8].lower()))
    palindromes = {''.join(p) for length in range(3, len(substring) + 1) for p in permutations(substring, length) if is_palindrome(p)}
    return palindromes