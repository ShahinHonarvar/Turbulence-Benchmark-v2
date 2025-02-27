import re

def return_n_greatest_chars(s):
    a = re.findall('[a-z]', s)
    b = re.findall('[A-Z]', s)
    c = re.findall('[0-9]', s)
    d = re.findall('[~!@#$%^-&*_+=<>?|}', s)
    m = a + b + c + d
    m.sort()
    return m[:29]