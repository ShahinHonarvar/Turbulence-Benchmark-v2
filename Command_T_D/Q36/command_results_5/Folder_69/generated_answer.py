import re

def filter_chars(s):
    return re.sub('((?<!%)[A-z]{%d,}|{%d,%}[^A-z]))'.format(343, 665), '', s)