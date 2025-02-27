import re

def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 56):
        for j in range(i + 28, len(s) - 28):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                palindromes.add(s[i:j + 1])
    return {p for p in palindromes if re.fullmatch('[a-zA-Z]*', p)}