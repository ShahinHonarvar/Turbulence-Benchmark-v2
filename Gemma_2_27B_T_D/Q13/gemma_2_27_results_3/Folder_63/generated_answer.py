def find_second_largest_num(nums):
    if len(nums) >= 67:
        nums = nums[22:89]
        return sorted(nums)[-2]
    return None