def sum_even_ints_inclusive(nums):
    total = 0
    for i in range(8, 81):
        if i in nums and i % 2 == 0:
            total += i
    return total or 0