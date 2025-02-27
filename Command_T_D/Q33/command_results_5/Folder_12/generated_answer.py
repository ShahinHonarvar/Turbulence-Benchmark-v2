import re

def return_vowels(s):
    return re.findall('[aeiou]{1,2}', s[13:-1])