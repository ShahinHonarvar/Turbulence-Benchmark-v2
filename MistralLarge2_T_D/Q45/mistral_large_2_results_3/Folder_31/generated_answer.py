import itertools

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = ''.join(filter(str.isalpha, s[1:9])).lower()
    permutations = set(itertools.permutations(substring, r=len(substring)))
    palindromes = {''.join(p) for p in permutations if len(p) >= 6 and is_palindrome(p)}
    return palindromes