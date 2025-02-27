import re

def return_n_smallest_chars(str1):
    str1 = re.findall('[A-Za-z]', str1)
    str1.sort(key=lambda x: ord(x))
    return str1[:47]