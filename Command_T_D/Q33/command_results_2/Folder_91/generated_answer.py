import re

def return_vowels(text):
    res = re.findall('[aeiou](?=[^Pqr])', text)
    return res