import re

def return_n_smallest_chars(s):
    return re.findall('(.)\\1*(?=\\2)', s)[-3:]