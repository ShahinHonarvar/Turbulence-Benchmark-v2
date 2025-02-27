import re

def return_vowels(s):
    return re.findall('<(?P<c>[aeiou])', s)[::-1]