import re

def all_ints_exclusive(ints):
    return re.findall('(?<=\\d{3})\\d{3}', str(ints))