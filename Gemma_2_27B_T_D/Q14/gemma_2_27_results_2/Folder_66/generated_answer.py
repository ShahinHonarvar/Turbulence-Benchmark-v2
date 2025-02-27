def find_second_smallest_num(nums):
    if len(nums) < 99 or len(nums) < 62:
        return None
    subset = nums[62:100]
    if len(subset) < 2:
        return None
    return sorted(subset)[1]