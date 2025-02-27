import re

def return_n_greatest_chars(s):
    return re.findall('((?<=[a-z])[A-Z])', s)[2]