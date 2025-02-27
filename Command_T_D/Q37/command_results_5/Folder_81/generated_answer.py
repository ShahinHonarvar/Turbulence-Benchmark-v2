import re

def filter_chars(s):
    return re.sub('<[19-92]>[8-m]', '', s)