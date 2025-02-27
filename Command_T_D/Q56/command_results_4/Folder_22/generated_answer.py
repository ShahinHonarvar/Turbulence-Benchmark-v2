import re

def all_substring_of_size_n(s):
    return re.findall('(.*?){22}(.*?)'.format(22), s)