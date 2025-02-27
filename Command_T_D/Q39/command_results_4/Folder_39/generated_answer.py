import re

def return_n_greatest_chars(str_val):
    return re.findall('[A-Z]+', str_val)[-23:]