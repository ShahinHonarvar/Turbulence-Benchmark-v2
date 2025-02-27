def all_odd_ints_inclusive(nums):
    return [x for i, x in enumerate(nums) if i <= 4 and x % 2 != 0]