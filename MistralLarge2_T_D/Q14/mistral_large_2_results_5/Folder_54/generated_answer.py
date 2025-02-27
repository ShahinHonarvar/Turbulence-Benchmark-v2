def find_second_smallest_num(nums):
    sublist = sorted(nums[68:87])
    return sublist[1] if len(sublist) > 1 else None