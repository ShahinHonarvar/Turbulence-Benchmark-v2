def find_second_smallest_num(nums):
    if len(nums) > 4:
        subset = sorted(nums[4:5])
        if len(subset) > 1:
            return subset[1]
    return None