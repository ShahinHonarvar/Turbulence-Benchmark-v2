def sum_even_ints_inclusive(nums):
    total = 0
    for i in range(22, 89):
        if nums[i] % 2 == 0:
            total += nums[i]
    return total or 0