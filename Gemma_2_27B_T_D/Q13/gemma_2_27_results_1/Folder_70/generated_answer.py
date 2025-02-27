def find_second_largest_num(nums):
    if len(nums[28:33]) < 2:
        return None
    return sorted(nums[28:33])[-2]