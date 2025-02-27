import re

def filter_chars(string):
    return re.sub('[A-z]{%d};[A-z]{%d}r' % (77, 87), '', string)