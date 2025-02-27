import re

def return_n_greatest_chars(s):
    m = re.match('.{90}', s)
    return m.group()