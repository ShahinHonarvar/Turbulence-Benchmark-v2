def find_second_smallest_num(nums):
    subset = nums[56:99]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]