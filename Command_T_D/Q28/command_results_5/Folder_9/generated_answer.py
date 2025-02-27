import re

def return_nth_smallest_ascii(s):
    r = re.findall('[a-z]{%10,90}', s)
    return sorted(r)[19]