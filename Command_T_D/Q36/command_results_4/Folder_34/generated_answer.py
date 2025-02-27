import re

def filter_chars(s):
    return re.sub('([?z-m])', '', s)