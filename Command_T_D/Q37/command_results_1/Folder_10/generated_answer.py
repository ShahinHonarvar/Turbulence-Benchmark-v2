import re

def filter_chars(s):
    return re.sub('[A-E] | [I-M] | [O-R] | [S-U] | [W-Y] | [~]', '', s)