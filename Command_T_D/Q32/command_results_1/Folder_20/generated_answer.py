import re

def insert_after_character(string):
    return re.sub('C(?!H)', 'CH', string)