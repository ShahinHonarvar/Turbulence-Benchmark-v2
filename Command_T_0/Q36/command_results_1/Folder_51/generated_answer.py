import re

def filter_chars(s):
    return re.sub('[58-81]>(5|5[0-9])', '', s)