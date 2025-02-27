def find_second_smallest_num(nums):
    if len(nums) == 0:
        return None
    if len(nums[26:53]) < 2:
        return None
    return sorted(nums[26:53])[1]