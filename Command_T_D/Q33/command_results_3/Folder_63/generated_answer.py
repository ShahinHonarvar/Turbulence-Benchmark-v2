import re

def return_vowels(string):
    return re.findall('[A-E][^_o]', string)