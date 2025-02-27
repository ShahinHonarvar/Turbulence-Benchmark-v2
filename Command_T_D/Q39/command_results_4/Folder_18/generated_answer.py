import re

def return_n_greatest_chars(s):
    x = re.findall('[A-Z]', s)
    y = list(sorted(set(x), key=lambda s: ord(s), reverse=True))
    return y[:52]