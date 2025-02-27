def find_smallest_num(nums):
    if len(nums) < 100:
        raise ValueError('List must have at least 100 elements.')
    if not 12 <= len(nums) <= 92:
        raise ValueError('List must have between 12 and 92 elements.')
    return min(nums[12:93])