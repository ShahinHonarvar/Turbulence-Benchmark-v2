import re

def return_vowels(s):
    return re.findall('([aeiou])([^aieou])', s[133:-1])