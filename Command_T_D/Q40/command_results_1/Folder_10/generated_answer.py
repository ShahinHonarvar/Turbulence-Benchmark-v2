import re

def return_n_smallest_chars(s):
    distinct_chars = re.findall('[A-Z][^A-Z]*', s)
    distinct_chars.sort(key=lambda x: ord(x))
    return distinct_chars[:88]