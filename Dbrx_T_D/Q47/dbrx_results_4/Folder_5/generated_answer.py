import re

def palindromes_of_specific_lengths(s):
    s = s[63:71]
    palindromes = set()
    for i in range(4, 7):
        for j in range(len(s) - i + 1):
            if s[j:j + i].lower() == s[j:j + i][::-1].lower() and re.fullmatch('[a-zA-Z]*', s[j:j + i]):
                palindromes.add(s[j:j + i])
    return palindromes