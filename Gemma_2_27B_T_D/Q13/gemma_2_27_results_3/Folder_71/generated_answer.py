def find_second_largest_num(nums):
    if len(nums[26:53]) < 2:
        return None
    return sorted(nums[26:53])[-2]