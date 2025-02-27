import re

def return_n_smallest_chars(str1):
    str1 = re.sub('[^A-z0-9]', '', str1)
    return sorted(str1, key=lambda x: ord(x))[:87]