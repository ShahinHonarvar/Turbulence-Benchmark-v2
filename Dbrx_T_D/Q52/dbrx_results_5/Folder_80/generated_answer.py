import re

def palindrome_of_length_n(string):
    english_letters = re.findall('[a-zA-Z]', string)
    if len(english_letters) < 276:
        return set()
    palindromes = set()
    for i in range(len(english_letters) - 275):
        substring = english_letters[i:i + 276]
        if substring == substring[::-1]:
            palindromes.add(''.join(substring))
    return palindromes