def find_second_largest_num(nums):
    if len(nums) < 42 or len(set(nums)) != len(nums):
        return None
    return sorted(nums[31:73])[-2]