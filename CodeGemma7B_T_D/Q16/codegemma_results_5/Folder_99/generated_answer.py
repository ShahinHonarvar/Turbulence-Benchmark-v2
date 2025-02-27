def sum_even_ints_inclusive(nums):
    total = 0
    for idx in range(310, 371):
        if idx >= len(nums):
            continue
        if nums[idx] % 2 == 0:
            total += nums[idx]
    return total or 0