def find_second_smallest_num(nums):
    if len(nums) < 56:
        return None
    subset = nums[34:56]
    if len(subset) < 2:
        return None
    return sorted(subset)[1]