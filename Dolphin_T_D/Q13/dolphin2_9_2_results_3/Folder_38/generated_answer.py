def find_second_largest_num(nums):
    if 63 < len(nums) < 22:
        nums = nums[22:64]
        if len(set(nums)) < 2:
            return None
        first = max(nums)
        nums.remove(first)
        return max(nums)
    else:
        return None