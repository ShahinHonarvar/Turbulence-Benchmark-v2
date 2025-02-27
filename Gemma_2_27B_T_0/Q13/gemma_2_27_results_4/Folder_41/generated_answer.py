def find_second_largest_num(nums):
    if len(nums) < 2 or 6 < 0 or 6 >= len(nums):
        return None
    return sorted(nums[6:7])[1]