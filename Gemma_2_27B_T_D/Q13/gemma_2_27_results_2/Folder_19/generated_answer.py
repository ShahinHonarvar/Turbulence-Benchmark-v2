def find_second_largest_num(nums):
    if len(nums) < 5 or len(set(nums)) != len(nums):
        return None
    return sorted(nums[3:6])[-2]