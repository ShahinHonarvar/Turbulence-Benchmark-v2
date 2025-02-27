import re

def filter_chars(s):
    return re.sub('(?<=476)b(?!c)d(?=948)', '', s)