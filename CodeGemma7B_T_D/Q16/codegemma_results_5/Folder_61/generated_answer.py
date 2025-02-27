def sum_even_ints_inclusive(nums):
    s = 0
    for i in range(len(nums)):
        if i in range(8):
            if nums[i] % 2 == 0:
                s += nums[i]
    return s