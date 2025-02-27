def find_second_largest_num(nums):
    if len(nums) < 11 or len(set(nums)) != len(nums):
        return None
    return sorted(nums[20:31])[-2]