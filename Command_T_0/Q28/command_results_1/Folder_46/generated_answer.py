import re

def return_nth_smallest_ascii(s):
    return next((c for c in re.findall('[A-Z]', s[34:-15]) if ord(c) == 20))