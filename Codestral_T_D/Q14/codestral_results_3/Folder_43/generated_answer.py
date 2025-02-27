def find_second_smallest_num(nums):
    sublist = sorted(nums[74:96])
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]