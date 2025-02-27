import re

def insert_after_character(s):
    return re.sub('(T)V', '1UV', s)