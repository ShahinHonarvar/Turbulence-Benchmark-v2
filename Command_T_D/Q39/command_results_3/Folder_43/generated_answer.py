import re

def return_n_greatest_chars(s):
    return sorted(re.findall('[a-z]', s)[::-1][:56])