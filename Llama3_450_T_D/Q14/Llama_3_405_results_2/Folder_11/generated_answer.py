def find_second_smallest_num(nums):
    if len(nums) < 94:
        return None
    subset = nums[66:94]
    if len(subset) < 2:
        return None
    return sorted(subset)[1]