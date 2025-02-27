import re

def return_vowels(s):
    vowels = re.findall('[aeiou]', s[46:90])
    return [''.join(vowels)] if vowels else []