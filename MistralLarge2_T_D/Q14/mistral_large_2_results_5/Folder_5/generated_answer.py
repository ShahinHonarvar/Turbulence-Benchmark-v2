def find_second_smallest_num(nums):
    sublist = sorted(nums[3:6])
    return sublist[1] if len(sublist) > 1 else None