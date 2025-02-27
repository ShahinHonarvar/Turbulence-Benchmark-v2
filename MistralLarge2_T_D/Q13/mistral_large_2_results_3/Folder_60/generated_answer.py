def find_second_largest_num(nums):
    subset = nums[75:86]
    if len(subset) < 2:
        return None
    largest = max(subset)
    subset.remove(largest)
    return max(subset)