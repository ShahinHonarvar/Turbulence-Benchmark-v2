def find_second_largest_num(nums):
    if len(nums[32:36]) < 2:
        return None
    return sorted(nums[32:36])[-2]