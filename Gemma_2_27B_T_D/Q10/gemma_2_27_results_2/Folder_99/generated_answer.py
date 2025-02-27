def all_odd_ints_exclusive(nums):
    return [x for i, x in enumerate(nums) if i >= 295 and i < 573 and (x % 2 != 0)]