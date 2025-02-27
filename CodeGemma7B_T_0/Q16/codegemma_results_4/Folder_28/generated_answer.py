def sum_even_ints_inclusive(nums):
    sum = 0
    for i in range(62, 64):
        if i >= len(nums):
            continue
        if nums[i] % 2 == 0:
            sum += nums[i]
    return sum