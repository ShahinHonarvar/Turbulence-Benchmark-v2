import re

def all_substring_of_size_n(s):
    for m in re.finditer('((?=.){146})', s):
        yield m.group()