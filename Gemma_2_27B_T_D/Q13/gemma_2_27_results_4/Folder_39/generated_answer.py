def find_second_largest_num(nums):
    if len(nums[20:31]) < 2:
        return None
    return sorted(nums[20:31])[-2]