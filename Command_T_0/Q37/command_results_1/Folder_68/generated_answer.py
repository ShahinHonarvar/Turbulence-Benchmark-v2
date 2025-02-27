import re

def filter_chars(s):
    return re.sub('(?<=.)(6[a-w])', '', s)