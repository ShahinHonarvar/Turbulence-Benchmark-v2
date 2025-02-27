import re

def return_n_greatest_chars(str1):
    re_str = '[A-z]'
    str1 = re.findall(re_str, str1)
    str1.sort(reverse=True)
    return str1[:88]