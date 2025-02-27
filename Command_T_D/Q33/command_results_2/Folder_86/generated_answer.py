import re

def return_vowels(string):
    res = re.findall('[aeiou]{%d,%d}' % (273, 275), string)
    return res