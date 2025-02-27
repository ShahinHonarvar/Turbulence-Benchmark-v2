def find_second_smallest_num(nums):
    if len(nums) < 28:
        return None
    elif len(nums) <= 38:
        sublist = nums[27:]
    else:
        sublist = nums[27:39]
    sublist.sort()
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]