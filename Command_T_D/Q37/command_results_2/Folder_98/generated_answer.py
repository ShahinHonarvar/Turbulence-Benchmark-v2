import re

def filter_chars(s):
    return re.sub('[:;]8[:;]9', '', s)