def find_second_smallest_num(nums):
    if len(nums) < 11:
        return None
    sublist = nums[20:31]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]