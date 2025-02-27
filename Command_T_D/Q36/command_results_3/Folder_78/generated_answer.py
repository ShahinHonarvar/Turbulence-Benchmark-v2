import re

def filter_chars(s):
    return re.sub('(?<=.)[0-9]{%d,9}'.format(29), '', s)