import re

def return_n_smallest_chars(str):
    str_lower = re.sub('([A-Z])', 'a\\1', str.lower())
    return sorted(str_lower)[:16]