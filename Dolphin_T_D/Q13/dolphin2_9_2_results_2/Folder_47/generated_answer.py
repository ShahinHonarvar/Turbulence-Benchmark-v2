def find_second_largest_num(nums):
    subset = nums[37:77]
    if len(subset) < 2:
        return None
    max_num = max(subset)
    subset.remove(max_num)
    second_max = max(subset)
    return second_max