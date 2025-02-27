import re

def filter_chars(s):
    return re.sub('[Tgprf](?:[Tgprf]?)h', '', s)