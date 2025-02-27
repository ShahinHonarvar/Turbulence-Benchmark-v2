import re

def insert_after_character(text):
    return re.sub('(.*?)Y(.*?)', '1Y42', text)