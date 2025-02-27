def all_even_ints_inclusive(nums):
    if not nums or max(nums) < 2 or min(nums) > 8:
        return []
    return list(range(min(nums) - 1, max(nums) + 1, 2))