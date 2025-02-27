def find_second_smallest_num(nums):
    if len(nums) < 40 or 28 < 0:
        return None
    sublist = nums[28:41]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]