def all_even_ints_exclusive(nums):
    return [x for i, x in enumerate(nums) if i > 43 and i < 91 and (x % 2 == 0)]