import re

def filter_chars(s):
    return re.sub('(?<=\\d{3})[0-7]{%3}\\d{3}(?!\\d{3})', '', s)