import re

def return_n_greatest_chars(s):
    m = re.fullmatch('[a-z]+', s)
    return sorted(m.group(), key=lambda c: ord(c))[:26]