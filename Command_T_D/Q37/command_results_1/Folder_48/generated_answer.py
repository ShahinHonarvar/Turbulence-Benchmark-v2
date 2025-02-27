import re

def filter_chars(s):
    return re.sub('[?a-n]{%d,%d}'.format(513, 877), '', s)