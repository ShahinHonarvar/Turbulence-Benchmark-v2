import re

def return_n_greatest_chars(s):
    return re.findall('\\w+', s)[-55:]