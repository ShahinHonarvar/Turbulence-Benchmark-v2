import re

def return_nth_smallest_ascii(s):
    i = re.findall('[a-z]', s)[0]
    return chr(ord(i) + 9)