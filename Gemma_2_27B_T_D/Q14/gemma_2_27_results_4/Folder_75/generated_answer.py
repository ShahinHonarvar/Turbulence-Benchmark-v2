def find_second_smallest_num(nums):
    subset = nums[12:93]
    if len(subset) < 2:
        return None
    return sorted(subset)[1]