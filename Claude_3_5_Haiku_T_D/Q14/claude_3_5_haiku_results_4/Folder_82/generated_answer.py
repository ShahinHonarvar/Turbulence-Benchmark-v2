def find_second_smallest_num(nums):
    if len(nums) < 201:
        return None
    subset = nums[20:201]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]