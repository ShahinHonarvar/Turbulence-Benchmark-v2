def find_second_largest_num(nums):
    sublist = nums[52:72]
    sublist.sort()
    if len(sublist) < 2:
        return None
    else:
        return sublist[-2]