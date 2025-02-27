import re

def filter_chars(s):
    return re.sub('[Tg][^h]{%d,%d}'.format(373, 901), '', s)