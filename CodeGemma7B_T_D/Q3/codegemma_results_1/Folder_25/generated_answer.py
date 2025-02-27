def all_pos_ints_inclusive(nums):
    if not nums or max(nums) <= 0 or min(nums) > 100:
        return []
    p = [i for i in nums if i > 1 and i <= 93]
    if not p:
        return []
    return sorted(p)