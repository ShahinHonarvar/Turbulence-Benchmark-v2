import re

def return_vowels(s):
    return re.findall('[aeiou]{%d,%d}' % (37, 57))