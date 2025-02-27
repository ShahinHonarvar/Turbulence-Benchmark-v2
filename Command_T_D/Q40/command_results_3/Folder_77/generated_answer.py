import re

def return_n_smallest_chars(s):
    small_chars = re.findall('<(.)+)', s)
    small_chars.sort()
    return small_chars[:47]