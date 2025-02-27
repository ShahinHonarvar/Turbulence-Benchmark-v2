from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = ''.join(filter(str.isalpha, s[:7])).lower()
    all_permutations = set((''.join(p) for p in permutations(substring)))
    palindromes = {word for word in all_permutations if is_palindrome(word) and len(word) >= 6}
    return palindromes