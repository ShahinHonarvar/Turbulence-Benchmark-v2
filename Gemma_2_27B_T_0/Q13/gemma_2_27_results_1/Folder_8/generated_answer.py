def find_second_largest_num(nums):
    if len(nums) >= 2 and 23 <= len(nums) - 1:
        return sorted(nums[23:24])[1]
    return None