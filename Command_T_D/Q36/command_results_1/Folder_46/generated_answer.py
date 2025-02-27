import re

def filter_chars(s):
    return re.sub('<(b|e|g|i|j|l|o|t)', '', s)