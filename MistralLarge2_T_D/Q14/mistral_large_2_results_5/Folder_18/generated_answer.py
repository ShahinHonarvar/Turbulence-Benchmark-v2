def find_second_smallest_num(nums):
    if nums:
        subset = sorted(nums[30:49])
        if len(subset) >= 2:
            return subset[1]
    return None