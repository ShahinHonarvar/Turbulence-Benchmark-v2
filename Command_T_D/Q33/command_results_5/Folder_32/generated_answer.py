import re

def return_vowels(s):
    return re.findall('[aeiou][^b]*[a-z]', s)