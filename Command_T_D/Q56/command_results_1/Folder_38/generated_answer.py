import re

def all_substring_of_size_n(s):
    if not s:
        return []
    return re.findall('([^{]+){35}', s)