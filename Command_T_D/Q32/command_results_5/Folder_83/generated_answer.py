import re

def insert_after_character(s):
    return re.sub('(E)(e)', '1e', s)