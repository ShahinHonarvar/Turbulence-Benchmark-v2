from functools import partial
from itertools import islice

def find_second_smallest_num(nums):
    small_list = sorted(nums)[33:37]
    if small_list:
        return small_list[1]
    else:
        return None