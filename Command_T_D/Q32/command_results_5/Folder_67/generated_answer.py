import re

def insert_after_character(s):
    return re.sub('j(?!1)', '11', s)