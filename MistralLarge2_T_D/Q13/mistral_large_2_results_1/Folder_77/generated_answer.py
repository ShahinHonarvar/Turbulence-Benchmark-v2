def find_second_largest_num(nums):
    subset = nums[527:539]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2]