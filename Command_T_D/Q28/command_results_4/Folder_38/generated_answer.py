import re

def return_nth_smallest_ascii(s):
    return next((char for i, char in enumerate(re.findall('[a-z]', s), 1) if ord(char) < ord('g') and i == 10))