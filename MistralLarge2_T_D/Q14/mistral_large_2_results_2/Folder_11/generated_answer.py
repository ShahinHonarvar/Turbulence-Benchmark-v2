def find_second_smallest_num(nums):
    if len(nums) <= 93:
        subset = nums[66:94]
        if len(subset) >= 2:
            return sorted(subset)[1]
    return None