import re

def filter_chars(s):
    return re.sub('((?<=.)[A-F0-9])([A-Z])', '\x01_', s)