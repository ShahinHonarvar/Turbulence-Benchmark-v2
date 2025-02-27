import re

def return_n_smallest_chars(s):
    i = re.findall('<([^>]+)>', s)
    return sorted(set(i), key=lambda x: ord(x))[:76]