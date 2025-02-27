import re

def palindromes_of_specific_lengths(text):
    return set(re.findall('[A-Z]+\\d{50,100}', text[100:-100]))