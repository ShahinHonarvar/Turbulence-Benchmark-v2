import re

def return_n_greatest_chars(s):
    char_list = re.findall('[A-Z]', s)
    char_list.sort(key=lambda x: ord(x))
    return char_list[:59]