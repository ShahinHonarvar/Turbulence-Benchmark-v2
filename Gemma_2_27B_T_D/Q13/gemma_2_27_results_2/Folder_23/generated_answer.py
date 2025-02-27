def find_second_largest_num(nums):
    if len(nums) < 20:
        return None
    part = nums[52:72]
    part.sort()
    if len(part) < 2:
        return None
    return part[-2]