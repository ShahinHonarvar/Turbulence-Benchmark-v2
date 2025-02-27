def all_odd_ints_exclusive(nums):
    return [n for i, n in enumerate(nums) if i > 65 and i < 90 and (n % 2 != 0)]