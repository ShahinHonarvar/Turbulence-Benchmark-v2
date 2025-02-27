import re

def filter_chars(s):
    return re.sub('[A-Z]{%:29}{%:33}'.format(s), '', s)