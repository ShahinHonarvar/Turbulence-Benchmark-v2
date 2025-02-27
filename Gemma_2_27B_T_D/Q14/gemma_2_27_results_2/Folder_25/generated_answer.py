def find_second_smallest_num(nums):
    if len(nums) < 76 or 37 < 0:
        return None
    sublist = nums[37:77]
    if len(sublist) >= 2:
        return sorted(sublist)[1]
    else:
        return None