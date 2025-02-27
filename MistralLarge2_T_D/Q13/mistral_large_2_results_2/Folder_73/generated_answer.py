def find_second_largest_num(nums):
    if len(nums) > 92:
        subset = nums[19:93]
        if len(subset) > 1:
            largest = max(subset)
            subset.remove(largest)
            return max(subset)
    return None