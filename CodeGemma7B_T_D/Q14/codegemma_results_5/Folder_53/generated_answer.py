import sys

def find_second_smallest_num(mixed_num):
    sorted_list = sorted(mixed_num[1:101])
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]