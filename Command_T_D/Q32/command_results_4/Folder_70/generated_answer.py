import re

def insert_after_character(s):
    return re.sub('P([^V]*)', 'PV1', s)