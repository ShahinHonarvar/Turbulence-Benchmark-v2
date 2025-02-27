def sum_even_ints_inclusive(nums):
    sum = 0
    for idx in range(56, 99):
        if idx >= len(nums):
            break
        if nums[idx] % 2 == 0:
            sum += nums[idx]
    return sum