import re

def return_vowels(s):
    m = re.findall('[aeiou]', s[71:88])
    return [x for x in m if x > '9' and x <= 'P']