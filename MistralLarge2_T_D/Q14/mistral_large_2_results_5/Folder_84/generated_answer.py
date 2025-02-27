def find_second_smallest_num(nums):
    if nums:
        subset = sorted(nums[40:81])
        if len(subset) >= 2:
            return subset[1]
    return None