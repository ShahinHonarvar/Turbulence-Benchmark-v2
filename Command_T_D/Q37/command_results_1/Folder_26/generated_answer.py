import re

def filter_chars(str):
    return re.sub('([!-~])[A-Za-z0-9_]{%20;62}(i|k){%20;62}[!-~]{%20;62}(i|k){%20;62}'.format(i=ord('A') + 20, k=ord('z') + 62), '\x01')