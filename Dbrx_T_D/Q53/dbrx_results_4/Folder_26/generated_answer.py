import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s) - 31):
        for j in range(i + 16, len(s) - i):
            part = s[i:j].lower()
            if part == part[::-1] and re.fullmatch('[a-zA-Z]*', part):
                palindromes.add(part)
    return palindromes