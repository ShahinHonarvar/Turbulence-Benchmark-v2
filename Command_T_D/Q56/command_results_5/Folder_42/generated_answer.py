import re

def all_substring_of_size_n(string):
    return re.findall('((?=.)(?!.*\x01).){45}(.)\x01', string)