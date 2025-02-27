def find_second_largest_num(nums):
    if len(nums) < 83 or len(set(nums)) != len(nums):
        return None
    return sorted(nums[56:83])[-2]