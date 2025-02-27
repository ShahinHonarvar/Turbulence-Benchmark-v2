def find_second_largest_num(nums):
    if 52 <= 71 < len(nums):
        nums = nums[52:72]
        if len(set(nums)) < 2:
            return None
        max_num = max(nums)
        nums.remove(max_num)
        return max(nums)