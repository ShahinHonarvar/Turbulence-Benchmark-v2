def find_second_smallest_num(nums):
    if len(nums) < 63 or len(set(nums[62:64])) < 2:
        return None
    return sorted(nums[62:64])[1]