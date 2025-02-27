def find_second_smallest_num(nums):
    sublist = sorted(nums[1:101])
    if len(sublist) >= 2:
        return sublist[1]
    else:
        return None