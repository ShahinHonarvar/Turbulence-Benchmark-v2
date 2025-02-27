import re

def return_n_greatest_chars(s):
    return re.findall('[A-Z]', sorted(re.findall('[A-Z]', s), reverse=True))