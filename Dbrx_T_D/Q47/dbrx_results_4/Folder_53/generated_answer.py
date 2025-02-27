import re

def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(3, 11):
        for i in range(1, 300 - length + 1):
            if s[i:i + length] == s[i:i + length][::-1] and re.fullmatch('[a-zA-Z]+', s[i:i + length]):
                palindromes.add(s[i:i + length])
    return palindromes