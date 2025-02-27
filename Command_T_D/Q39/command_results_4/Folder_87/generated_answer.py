import re

def return_n_greatest_chars(s):
    str_list = re.findall('[A-Z]', s)
    max_list = list(sorted(str_list))[:24]
    return max_list