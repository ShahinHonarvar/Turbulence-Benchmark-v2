import re

def filter_chars(s):
    return re.sub('[lmnpqrstuvy]', '', s)