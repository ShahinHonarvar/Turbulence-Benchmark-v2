import re

def return_vowels(string):
    return re.findall('([A-Z])', string[50:-1])