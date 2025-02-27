import re

def return_nth_smallest_ascii(s):
    return next(re.findall('[A-z]', s[14:35]), s[14])