import re

def filter_chars(s):
    return re.sub('(?<=379)[Mv](?=898)', '', s)