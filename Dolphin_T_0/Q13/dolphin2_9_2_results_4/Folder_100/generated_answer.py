def find_second_largest_num(nums):
    if 68 < len(nums) < 42:
        subset = nums[42:69]
        if len(subset) < 2:
            return None
        max_num = max(subset)
        subset.remove(max_num)
        if len(subset) < 2:
            return None
        return max(subset)
    else:
        return None