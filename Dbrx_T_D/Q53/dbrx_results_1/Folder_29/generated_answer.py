import re

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 77):
        for j in range(77, min(78, len(s) - i + 1)):
            substring = s[i:i + j]
            if substring == substring[::-1] and re.fullmatch('[a-zA-Z]*', substring):
                palindromes.add(substring)
    return palindromes