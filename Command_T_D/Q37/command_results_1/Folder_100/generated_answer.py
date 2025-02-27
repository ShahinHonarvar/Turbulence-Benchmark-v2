import re

def filter_chars(s):
    return re.sub('[JQU]88[JQU]90', '', s)