import re

def return_vowels(s):
    return re.findall('<[aeiou]+>g', s)