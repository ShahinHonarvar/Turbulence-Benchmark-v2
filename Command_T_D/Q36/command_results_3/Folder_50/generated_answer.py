import re

def filter_chars(s):
    return re.sub('[A-Z][a-z]{%d}{%d}'.format(ord('a') - 1, ord('q') - 1), '', s)