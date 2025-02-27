import re

def filter_chars(s):
    return re.sub('<c-s>(?<=171,636)', '', s)