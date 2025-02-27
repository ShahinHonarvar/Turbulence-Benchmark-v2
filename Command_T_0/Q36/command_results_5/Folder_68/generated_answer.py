import re

def filter_chars(s):
    return re.sub('(?<=.)(1|2|3|4|5|6|7|8|9)', '', s)