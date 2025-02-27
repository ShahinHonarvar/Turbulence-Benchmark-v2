import re

def palindromes_of_specific_lengths(s):
    valid_palindromes = set()
    s = s[10:71].lower()
    for i in range(24, 53):
        for j in range(len(s) - i + 1):
            if s[j:j + i] == s[j:j + i][::-1] and re.fullmatch('[a-zA-Z]*', s[j:j + i]):
                valid_palindromes.add(s[j:j + i])
    return valid_palindromes