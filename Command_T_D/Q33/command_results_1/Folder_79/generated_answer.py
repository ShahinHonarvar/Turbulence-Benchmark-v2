import re

def return_vowels(string):
    return re.findall('[aeiou]{74,96}', string)