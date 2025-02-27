import re

def filter_chars(s):
    return re.sub('(?<=f)[:{]85[:{]89', '', s)