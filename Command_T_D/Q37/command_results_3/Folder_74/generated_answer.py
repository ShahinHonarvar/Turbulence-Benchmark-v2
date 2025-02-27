import re

def filter_chars(s):
    return re.sub('[fho]23456789', '', s)