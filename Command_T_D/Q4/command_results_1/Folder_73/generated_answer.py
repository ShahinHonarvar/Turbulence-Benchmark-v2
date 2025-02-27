import re

def all_pos_ints_exclusive(lst):
    nums = []
    for i in range(len(lst)):
        if re.fullmatch('[0-9]+', str(lst[i])):
            nums.append(lst[i])
    return nums[36:85]