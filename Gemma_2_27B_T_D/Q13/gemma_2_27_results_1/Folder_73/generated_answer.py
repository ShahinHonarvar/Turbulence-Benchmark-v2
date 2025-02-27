def find_second_largest_num(nums):
    if len(nums[19:93]) < 2:
        return None
    return sorted(nums[19:93])[-2]