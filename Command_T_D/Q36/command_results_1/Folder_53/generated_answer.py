import re

def filter_chars(s):
    return re.sub('c<90,97>', '', s)