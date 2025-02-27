def all_even_ints_exclusive(nums):
    return [x for i, x in enumerate(nums) if i >= 41 and i < 69 and (x % 2 == 0)]