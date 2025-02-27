import re

def filter_chars(str):
    return re.sub('(?!<10)>(?!79)<[?a-m]', '', str)