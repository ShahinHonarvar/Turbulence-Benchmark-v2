import re

def insert_after_character(s):
    return re.sub('0(?!4)', '04', s)