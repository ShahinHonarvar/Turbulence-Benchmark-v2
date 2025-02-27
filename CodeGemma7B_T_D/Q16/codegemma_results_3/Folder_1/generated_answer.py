def sum_even_ints_inclusive(nums):
    i = 31
    s = 0
    while i <= 72:
        if nums[i] % 2 == 0:
            s += nums[i]
        i += 1
    return s