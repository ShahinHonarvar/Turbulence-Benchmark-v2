from functools import partial

def find_second_smallest_num(nums):
    sublist = sorted(nums)[31:35]
    return sublist[1] if len(sublist) > 1 else 'None'