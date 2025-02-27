import re

def return_nth_smallest_ascii(s):
    return next((r for r in range(ord('z') + 1) if re.fullmatch('<[a-z]', chr(r))))