def sum_even_ints_inclusive(nums):
    acc = 0
    for i in range(5):
        if nums[i] % 2 == 0:
            acc += nums[i]
    return acc