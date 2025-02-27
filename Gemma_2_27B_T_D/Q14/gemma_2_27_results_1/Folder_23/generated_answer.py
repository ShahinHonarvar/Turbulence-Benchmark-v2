def find_second_smallest_num(nums):
    if len(nums) < 92 or len(nums) <= 19 or len(set(nums)) != len(nums):
        return None
    return sorted(nums[19:93])[1]