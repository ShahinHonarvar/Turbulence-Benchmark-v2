def find_second_largest_num(nums):
    if len(nums) < 93 or len(set(nums)) != len(nums):
        return None
    return sorted(nums[62:93])[-2]