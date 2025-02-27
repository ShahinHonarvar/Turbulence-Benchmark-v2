import re

def all_substring_of_size_n(string):
    return [re.sub('(.)\x01+', '\x01', s) for s in re.findall('(.)\x01*', string)]