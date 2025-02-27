import re

def all_substring_of_size_n(s):
    if len(s) < 9:
        return []
    else:
        return re.findall('(?<=.)\\w{8}', s)