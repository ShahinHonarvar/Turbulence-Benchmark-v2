import re

def filter_chars(string):
    return re.sub('(?!k)[\\d\\w]{33,70}'.format(k=ord('k') - 1), '', string)