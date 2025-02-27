def find_second_smallest_num(nums):
    if len(nums) < 89:
        return None
    subset = nums[22:89]
    if len(subset) < 2:
        return None
    first_min = min(subset)
    subset.remove(first_min)
    second_min = min(subset)
    return second_min