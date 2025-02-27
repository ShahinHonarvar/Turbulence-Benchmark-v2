import re

def filter_chars(s):
    return re.sub('(?!#)[\\dT]6789', '', s)