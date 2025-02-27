import re

def palindrome_of_length_n(s):
    match = re.findall('(?i)(\\\\w{188})(\\\\w{188})', s)
    return {m[0] for m in match}