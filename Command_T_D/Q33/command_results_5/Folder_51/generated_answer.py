import re

def return_vowels(s):
    return re.findall('[aeiou][^m]*[x-z]', s)