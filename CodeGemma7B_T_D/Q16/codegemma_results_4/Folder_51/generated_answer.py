def sum_even_ints_inclusive(nums):
    sum_even = 0
    for i in range(1, 9):
        if i % 2 == 0:
            try:
                sum_even += nums[i]
            except IndexError:
                pass
    return sum_even