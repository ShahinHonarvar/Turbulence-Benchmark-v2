def find_second_smallest_num(nums):
    if len(nums) < 86 or 68 < 0:
        return None
    sublist = nums[68:87]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]