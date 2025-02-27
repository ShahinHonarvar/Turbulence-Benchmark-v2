import re

def return_vowels(s):
    return re.findall('[aeiou]{%d,%d}' % (837, 975), s)