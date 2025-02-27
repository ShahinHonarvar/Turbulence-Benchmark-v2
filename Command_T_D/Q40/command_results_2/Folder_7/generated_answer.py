import re

def return_n_smallest_chars(s):
    matches = re.findall('([a-z])', s)
    characters = sorted(list(set(matches)), key=lambda x: ord(x))[:49]
    return characters