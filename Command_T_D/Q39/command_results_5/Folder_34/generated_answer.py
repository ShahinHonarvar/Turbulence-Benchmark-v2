import re

def return_n_greatest_chars(s):
    return re.findall('<(.)>', s)[-9:-1]