import re

def filter_chars(str):
    return re.sub('(?!%#)(?<=\\D)[b-~]', '', str)