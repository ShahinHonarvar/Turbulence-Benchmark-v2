import re

def insert_after_character(s):
    return re.sub('B([^N]*?)', 'BN1', s)