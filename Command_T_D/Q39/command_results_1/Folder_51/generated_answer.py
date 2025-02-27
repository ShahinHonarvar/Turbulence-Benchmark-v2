import re

def return_n_greatest_chars(s):
    return re.findall('(.)\x01*', s)[::-1][:45]