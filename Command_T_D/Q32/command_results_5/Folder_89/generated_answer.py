import re

def insert_after_character(text):
    return re.sub('([A-Z])', '1W', text)