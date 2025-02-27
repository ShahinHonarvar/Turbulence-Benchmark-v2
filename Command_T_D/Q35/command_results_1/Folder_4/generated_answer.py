import re

def remove_repeat_chars(s):
    return re.sub('[a-z]{%d,%d}{%d,%d}'.format(49, 74, 49, 74), '', s)