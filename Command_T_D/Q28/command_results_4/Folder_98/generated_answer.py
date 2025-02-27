import re

def return_nth_smallest_ascii(str):
    return next((char for i, char in enumerate(re.findall('[a-z]', str), start=9) if i < 9))