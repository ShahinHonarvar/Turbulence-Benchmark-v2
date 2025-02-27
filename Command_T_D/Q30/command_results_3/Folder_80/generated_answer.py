import re

def insert_before_character(s):
    return re.sub('(.)X(.)', '\\1XX\\2', s)