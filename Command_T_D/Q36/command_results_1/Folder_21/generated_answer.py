import re

def filter_chars(s):
    return re.sub('(?<=.)([!*+<>?]#43)(?=.)', '', s)