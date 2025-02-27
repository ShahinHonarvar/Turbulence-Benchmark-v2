def find_second_largest_num(nums):
    if len(nums) < 557:
        return None
    subset = nums[209:557]
    if len(subset) < 2:
        return None
    first_largest = max(subset)
    subset.remove(first_largest)
    second_largest = max(subset)
    return second_largest