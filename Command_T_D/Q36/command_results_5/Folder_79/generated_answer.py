import re

def filter_chars(s):
    return re.sub('(?<=!)([A-Z]{{11,46}})', '', s)