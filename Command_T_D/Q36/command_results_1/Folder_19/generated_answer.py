import re

def filter_chars(s):
    return re.sub('([;]\\d){2}(r)', '', s)