import re

def return_nth_smallest_ascii(s):
    return re.findall('[A-Z]', s)[9]