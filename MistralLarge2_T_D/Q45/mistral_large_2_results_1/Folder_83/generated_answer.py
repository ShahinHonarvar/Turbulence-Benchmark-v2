from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = ''.join(filter(str.isalpha, s[2:10])).lower()
    all_permutations = set(permutations(substring))
    palindromes = {''.join(p) for p in all_permutations if len(p) >= 7 and is_palindrome(p)}
    return palindromes