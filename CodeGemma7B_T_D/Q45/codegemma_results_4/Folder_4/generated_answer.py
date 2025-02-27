from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    return {''.join(p) for p in permutations(filter(str.isalpha, s[3:10].lower())) if is_palindrome(p) and len(p) >= 7}