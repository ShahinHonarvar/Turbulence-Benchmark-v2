def find_second_smallest_num(nums):
    if 92 < len(nums):
        sublist = nums[62:93]
        if len(sublist) >= 2:
            return sorted(sublist)[1]
    return None