def find_second_smallest_num(nums):
    if len(nums) < 39 or len(set(nums)) != len(nums):
        return None
    return sorted(nums[28:39])[1]