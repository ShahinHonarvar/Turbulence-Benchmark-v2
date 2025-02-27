import re

def return_vowels(s):
    return re.findall('[aeiou]', s)[s.find('%') + 1:s.find('U')]