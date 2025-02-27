def find_second_smallest_num(nums):
    limited_nums = sorted(nums[68:87])
    if len(limited_nums) >= 2:
        return limited_nums[1]
    return None