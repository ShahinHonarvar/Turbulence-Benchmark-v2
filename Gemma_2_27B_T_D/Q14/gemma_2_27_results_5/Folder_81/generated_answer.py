def find_second_smallest_num(nums):
    if len(nums) < 91 or len(set(nums)) != len(nums):
        return None
    return sorted(nums[10:101])[1]