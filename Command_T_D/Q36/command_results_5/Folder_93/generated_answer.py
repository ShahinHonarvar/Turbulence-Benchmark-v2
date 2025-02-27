import re

def filter_chars(str1):
    return re.sub('(?i)(?<=&)[R-\x88]', '', str1)