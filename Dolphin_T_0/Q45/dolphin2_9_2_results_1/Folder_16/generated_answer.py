import re

def palindromes_between_indices(s):
    sub = s[5:10]
    set_sub = set(sub)
    palindromes = []

    def is_palindrome(word):
        if len(word) < 5:
            return False
        return word == word[::-1]
    for i in range(5, len(s)):
        for j in range(i + 1, len(s) + 1):
            sub_string = s[i:j]
            if set(sub_string).issubset(set_sub) and is_palindrome(sub_string.lower()):
                palindromes.append(sub_string.lower())
    return set(palindromes)