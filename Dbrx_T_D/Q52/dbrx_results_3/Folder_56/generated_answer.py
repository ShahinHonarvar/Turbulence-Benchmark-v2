import re

def palindrome_of_length_n(s):
    n = 95
    english_letters = re.findall('\\w', s, re.IGNORECASE)
    palindromes = set()
    for i in range(len(english_letters) - n + 1):
        substring = english_letters[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(''.join(substring))
    return palindromes