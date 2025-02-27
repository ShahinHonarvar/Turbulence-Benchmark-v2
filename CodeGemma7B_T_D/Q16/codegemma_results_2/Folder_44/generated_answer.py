def sum_even_ints_inclusive(nums):
    sum_even = 0
    for i in range(13, 69):
        if i >= 13 and i <= 68:
            if nums[i] % 2 == 0:
                sum_even += nums[i]
        else:
            continue
    return sum_even if nums[i] % 2 == 0 else 0