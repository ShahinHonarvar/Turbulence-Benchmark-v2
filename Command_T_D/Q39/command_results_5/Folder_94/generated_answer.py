import re

def return_n_greatest_chars(str_):
    str_ = re.sub('[^A-Z]', '', str_)
    list_ = str_.split('')
    list_ = list(sorted(list_, key=lambda x: ord(x)))[:87]
    return list_