def all_even_ints_exclusive(nums):
    return [x for i, x in enumerate(nums) if i >= 64 and i < 80 and (x % 2 == 0)]