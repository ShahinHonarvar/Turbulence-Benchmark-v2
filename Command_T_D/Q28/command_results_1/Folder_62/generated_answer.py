import re

def return_nth_smallest_ascii(s):
    return next((char for char in range(ord('a') + 1, ord('z') + 1) if re.fullmatch('[a-z]', chr(char))))