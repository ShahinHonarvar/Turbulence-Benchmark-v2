def all_even_ints_exclusive(nums):
    return [x for i, x in enumerate(nums) if x % 2 == 0 and 15 < i < 40]