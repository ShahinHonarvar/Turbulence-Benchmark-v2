import re

def return_vowels(s):
    return re.findall('[aeiou][^l]d', s)