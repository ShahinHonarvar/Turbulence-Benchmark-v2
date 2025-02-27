import re

def all_pos_ints_inclusive(int_list):
    return re.findall('\\d+', str(min(int_list[:12]))) + re.findall('\\d+', str(max(int_list[12:92])))