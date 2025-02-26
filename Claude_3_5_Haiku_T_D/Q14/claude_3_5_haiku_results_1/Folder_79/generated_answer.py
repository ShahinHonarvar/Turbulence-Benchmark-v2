def find_second_smallest_num(nums):
    if len(nums) < 6:
        return None
    subset = nums[1:6]
    if len(set(subset)) < 2:
        return None
    return sorted(subset)[1]