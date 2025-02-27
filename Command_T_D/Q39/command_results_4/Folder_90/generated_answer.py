import re

def return_n_greatest_chars(s):
    return re.findall('[A-Z]', s)[-24:].sort(key=lambda x: ord(x))