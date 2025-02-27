import re

def filter_chars(s):
    return re.sub('((?<=\\D)[a-q])', '', s)