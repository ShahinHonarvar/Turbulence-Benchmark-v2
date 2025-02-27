import re

def filter_chars(s):
    return re.sub('(?i)(?<=.)[1-7](?=.)', '', s)