from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[2:10])).lower()
    all_permutations = set((''.join(p) for i in range(6, len(letters) + 1) for p in permutations(letters, i)))
    return {p for p in all_permutations if is_palindrome(p)}