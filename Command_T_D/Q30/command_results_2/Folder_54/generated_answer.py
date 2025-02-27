import re

def insert_before_character(s):
    return re.sub('(?i)(M)', '\\1f', s)