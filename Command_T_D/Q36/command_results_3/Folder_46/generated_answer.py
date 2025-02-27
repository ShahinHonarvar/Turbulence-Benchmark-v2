import re

def filter_chars(s):
    return re.sub('<|19|C|69|>', '', s)