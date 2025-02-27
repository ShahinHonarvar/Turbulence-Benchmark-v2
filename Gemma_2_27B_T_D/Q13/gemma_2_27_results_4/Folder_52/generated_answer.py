def find_second_largest_num(nums):
    if len(nums) < 38 or len(set(nums)) != len(nums):
        return None
    return sorted(nums[28:39])[::-1][1]