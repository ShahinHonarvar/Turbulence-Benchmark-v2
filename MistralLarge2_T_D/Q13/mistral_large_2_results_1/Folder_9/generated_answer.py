def find_second_largest_num(nums):
    if len(nums) > 200:
        subset = nums[200:201]
        if len(subset) >= 2:
            subset.sort(reverse=True)
            return subset[1]
    return None