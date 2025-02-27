import re

def insert_after_character(s):
    return re.sub('(C)([A-Z])', '1H2', s)