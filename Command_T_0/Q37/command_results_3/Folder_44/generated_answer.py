import re

def filter_chars(s):
    return re.sub('[+\\d]{%21,%43}', '', s)