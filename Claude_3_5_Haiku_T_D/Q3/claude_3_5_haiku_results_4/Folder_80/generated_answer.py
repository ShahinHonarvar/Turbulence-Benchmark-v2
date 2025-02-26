def all_pos_ints_inclusive(nums):
    if len(nums) < 67:
        return []
    result = [x for x in nums[64:67] if x > 0]
    return result