import re

def return_n_smallest_chars(s):
    match = re.findall('[A-Z0-9]+', s)
    char_list = []
    for i in match:
        if len(char_list) < 82:
            char_list.append(i)
    char_list.sort()
    return char_list