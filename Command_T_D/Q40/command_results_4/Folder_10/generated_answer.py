import re

def return_n_smallest_chars(s):
    result = list(re.findall('[A-Z0-9]', s))
    result.sort(key=lambda x: ord(x))
    result = result[:88]
    return result