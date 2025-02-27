def find_second_smallest_num(nums):
    subset = nums[52:72]
    if len(subset) < 2:
        return None
    return sorted(subset)[1]