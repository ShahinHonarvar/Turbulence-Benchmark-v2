def find_second_smallest_num(nums):
    if not nums or len(nums) < 41:
        return None
    subset = nums[40:81]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]