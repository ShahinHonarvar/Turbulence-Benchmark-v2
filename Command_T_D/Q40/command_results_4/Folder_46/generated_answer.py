import re

def return_n_smallest_chars(str):
    return sorted(re.findall('[a-z]', str), key=lambda x: ord(x))[:54]