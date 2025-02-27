import re

def return_n_greatest_chars(s):
    re_str = re.sub('[^A-Z]', '', s)
    return re.findall('[A-Z]', re_str)[-35:][::-1]