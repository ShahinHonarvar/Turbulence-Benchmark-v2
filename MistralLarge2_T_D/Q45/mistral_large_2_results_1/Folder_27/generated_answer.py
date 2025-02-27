from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[2:9])).lower()
    all_permutations = set(permutations(letters, r=6))
    palindromes = {''.join(p) for p in all_permutations if is_palindrome(p)}
    return palindromes