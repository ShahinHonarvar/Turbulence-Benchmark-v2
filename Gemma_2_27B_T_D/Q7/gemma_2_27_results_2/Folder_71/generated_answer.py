def all_even_ints_inclusive(nums):
    return [x for i, x in enumerate(nums) if i >= 26 and i <= 52 and (x % 2 == 0)]