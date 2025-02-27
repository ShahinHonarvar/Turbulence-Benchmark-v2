import re

def return_n_greatest_chars(s):
    lst = re.findall('[A-Z]+', s)
    lst.sort(key=lambda x: ord(x))
    return lst[:61]