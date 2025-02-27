import re

def return_vowels(s):
    m = re.search('[aeiou]{%d,%d}[^|;]+' % (12, 39), s)
    return m.group()