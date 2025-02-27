import re

def return_n_greatest_chars(str):
    m = re.findall('[A-Z]', str)
    m.sort(key=lambda x: ord(x))
    return m[:57]