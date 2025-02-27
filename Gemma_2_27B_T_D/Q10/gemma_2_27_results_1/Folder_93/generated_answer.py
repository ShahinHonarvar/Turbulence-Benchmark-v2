def all_odd_ints_exclusive(nums):
    return [x for i, x in enumerate(nums) if x % 2 != 0 and 19 < i < 94]