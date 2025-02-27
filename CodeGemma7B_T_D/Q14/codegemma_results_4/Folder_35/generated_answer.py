from math import *

def find_second_smallest_num(num_list):
    if len(num_list) <= 15 or len(num_list) > 40:
        return None
    num_list.sort(key=lambda num: num)
    index_15th = 15 - 1
    return num_list[index_15th + 1] if len(num_list) - index_15th >= 2 else None