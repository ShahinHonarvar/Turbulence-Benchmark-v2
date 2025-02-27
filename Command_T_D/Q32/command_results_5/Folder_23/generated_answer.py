import re

def insert_after_character(text):
    return re.sub('b([^by]*)(?=by)', 'b1y', text)