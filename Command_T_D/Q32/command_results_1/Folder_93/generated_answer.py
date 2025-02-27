import re

def insert_after_character(string):
    return re.sub('(Y)(?!4)', 'Y4', string)