def sum_even_ints_inclusive(nums):
    return sum((i for i in nums[:9] if i % 2 == 0))