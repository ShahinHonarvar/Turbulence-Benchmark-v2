def find_second_largest_num(nums):
    if len(nums[15:52]) < 2:
        return None
    return sorted(nums[15:52])[-2]