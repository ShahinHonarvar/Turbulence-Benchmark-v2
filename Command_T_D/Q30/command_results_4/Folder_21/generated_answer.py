import re

def insert_before_character(s):
    return re.sub('((?<= )K) | ((?<= ) )', 'K\\1', s)