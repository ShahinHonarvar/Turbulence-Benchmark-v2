def find_second_smallest_num(nums):
    if len(nums) < 76 or 37 < 0:
        return None
    sublist = nums[37:77]
    sorted_sublist = sorted(sublist)
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]