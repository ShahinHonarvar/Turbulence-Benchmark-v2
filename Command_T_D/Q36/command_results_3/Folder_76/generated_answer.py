import re

def filter_chars(s):
    return re.sub('(?<=\\d)B(?!\\d)', '', s, flags=re.I)