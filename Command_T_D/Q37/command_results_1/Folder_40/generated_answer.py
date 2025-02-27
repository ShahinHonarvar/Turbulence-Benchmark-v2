import re

def filter_chars(s):
    return re.sub('(?<=\\A[^*])\\w+|(?<=\\s)\\w+', '', s)