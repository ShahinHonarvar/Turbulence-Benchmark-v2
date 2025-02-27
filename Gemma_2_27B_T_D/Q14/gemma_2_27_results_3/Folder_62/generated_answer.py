def find_second_smallest_num(nums):
    if len(nums) < 66:
        return None
    subset = nums[10:67]
    if len(subset) < 2:
        return None
    return sorted(subset)[1]