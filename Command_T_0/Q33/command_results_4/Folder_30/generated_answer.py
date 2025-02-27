import re

def return_vowels(s):
    return re.findall('[AEIOU][^M]*[A-W]', s)