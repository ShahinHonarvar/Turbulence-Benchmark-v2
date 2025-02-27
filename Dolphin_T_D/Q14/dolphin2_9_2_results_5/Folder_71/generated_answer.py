def find_second_smallest_num(nums):
    if 51 >= len(nums) >= 29:
        subset = nums[29:52]
        subset.sort()
        if len(subset) > 1:
            return subset[1]
    return None