def find_second_largest_num(nums):
    if len(nums) < 35 or len(set(nums)) != len(nums):
        return None
    return sorted(nums[25:60])[-2]