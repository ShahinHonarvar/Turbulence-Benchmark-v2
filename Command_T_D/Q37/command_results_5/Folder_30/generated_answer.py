import re

def filter_chars(s):
    return re.sub('(?<=K)[A-Z]+(?<=])', '', s)