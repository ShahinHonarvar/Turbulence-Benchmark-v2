def all_even_ints_inclusive(nums):
    return [i for i in nums if i % 2 == 0 and i in range(0, 11, 2)] or []