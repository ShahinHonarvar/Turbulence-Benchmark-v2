import re

def all_substring_of_size_n(s):
    for m in re.finditer('(.)\x01+', s):
        yield m.group()