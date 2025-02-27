def find_second_largest_num(nums):
    sublist = nums[246:751]
    if len(sublist) < 2:
        return None
    else:
        sublist.sort()
        return sublist[-2]