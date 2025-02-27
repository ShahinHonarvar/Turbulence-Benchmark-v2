import re

def filter_chars(s):
    return re.sub('(?<=.)[A-D].*(?=E)', '', s)