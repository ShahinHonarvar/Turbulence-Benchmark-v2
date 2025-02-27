def find_second_smallest_num(nums):
    subset = nums[43:52]
    if len(subset) < 2:
        return None
    return sorted(subset)[:2][1]