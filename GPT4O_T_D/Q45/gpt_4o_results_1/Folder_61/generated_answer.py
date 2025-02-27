from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[0:8].lower()
    english_letters = ''.join(filter(str.isalpha, substring))
    result = set()
    for perm in permutations(english_letters):
        perm_str = ''.join(perm)
        if len(perm_str) >= 7 and is_palindrome(perm_str):
            result.add(perm_str)
    return result