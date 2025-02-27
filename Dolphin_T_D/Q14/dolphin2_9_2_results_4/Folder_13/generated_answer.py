def find_second_smallest_num(nums):
    if not 28 <= len(nums) <= 32:
        return None
    if len(set(nums[28:33])) < 2:
        return None
    return sorted(nums[28:33])[1]