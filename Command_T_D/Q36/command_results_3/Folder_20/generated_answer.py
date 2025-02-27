import re

def filter_chars(s):
    return re.sub('(?<=\\d{13})([A-Z])(?<=\\d{40})', '', s)