def find_second_largest_num(nums):
    subset = nums[26:53]
    if len(subset) < 2:
        return None
    else:
        largest = max(subset)
        subset.remove(largest)
        second_largest = max(subset)
        return second_largest