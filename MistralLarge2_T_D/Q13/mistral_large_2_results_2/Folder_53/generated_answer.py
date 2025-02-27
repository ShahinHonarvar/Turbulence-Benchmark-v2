def find_second_largest_num(nums):
    if len(nums) > 200:
        subset = nums[100:201]
        if len(subset) > 1:
            first_largest = max(subset)
            subset.remove(first_largest)
            return max(subset)
    return None