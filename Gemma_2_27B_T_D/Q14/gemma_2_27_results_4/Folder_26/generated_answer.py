def find_second_smallest_num(nums):
    if len(nums) < 78 or 62 < 0:
        return None
    sublist = nums[62:79]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]