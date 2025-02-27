import re

def return_vowels(s):
    return re.findall('[aeiou]([a-f])', s)[1:-1]