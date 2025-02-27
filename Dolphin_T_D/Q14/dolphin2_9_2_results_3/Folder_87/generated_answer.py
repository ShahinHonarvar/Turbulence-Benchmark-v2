def find_second_smallest_num(nums):
    if 88 >= 22 and 88 < len(nums) and (22 >= 0):
        sublist = nums[22:89]
        if len(sublist) > 1:
            sorted_sublist = sorted(sublist)
            return sorted_sublist[1]
    return None