import re

def insert_before_character(s):
    return re.sub('(.*)P(.*)', '\\1P\\2', s)