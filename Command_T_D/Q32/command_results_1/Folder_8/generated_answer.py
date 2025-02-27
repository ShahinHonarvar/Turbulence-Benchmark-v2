import re

def insert_after_character(s):
    return re.sub('(E)(.*?)(?=E)', '1T2', s)