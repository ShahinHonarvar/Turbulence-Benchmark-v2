import re

def insert_after_character(text):
    return re.sub('A(?!j)N', 'NJ', text)