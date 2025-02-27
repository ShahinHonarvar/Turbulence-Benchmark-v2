import re

def all_substring_of_size_n(s):
    if not s:
        return []
    return [x for x in re.findall('(?<=.)\\w{25}', s)]