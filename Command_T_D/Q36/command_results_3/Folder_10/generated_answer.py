import re

def filter_chars(s):
    return re.sub('(?i)(?<=!)([A-Z])([A-Z]![A-Z]![A-Z]![A-Z])', '', s)