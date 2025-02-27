def find_second_smallest_num(nums):
    subset = nums[74:96]
    if len(subset) < 2:
        return None
    else:
        smallest = min(subset)
        subset.remove(smallest)
        second_smallest = min(subset)
        return second_smallest