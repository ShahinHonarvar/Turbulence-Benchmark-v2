import re

def return_nth_smallest_ascii(text):
    return re.sub('[A-Z]{%d,%d}', lambda m: str(ord(m.group()) + 7), text)[50:75]