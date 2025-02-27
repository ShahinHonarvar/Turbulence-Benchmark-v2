import re

def insert_before_character(s):
    return re.sub('(?<=T)V', 'V\\1', s)