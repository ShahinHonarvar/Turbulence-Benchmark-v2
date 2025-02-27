def find_second_smallest_num(nums):
    if not 200 >= len(nums) > 1:
        return None
    subset = sorted(nums[1:200])
    if len(subset) < 2:
        return None
    return subset[1]