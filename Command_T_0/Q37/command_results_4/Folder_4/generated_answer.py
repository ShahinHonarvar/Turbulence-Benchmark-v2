import re

def filter_chars(s):
    return re.sub('[a-z]{%19,%33}{%S,%{}}', '', s)