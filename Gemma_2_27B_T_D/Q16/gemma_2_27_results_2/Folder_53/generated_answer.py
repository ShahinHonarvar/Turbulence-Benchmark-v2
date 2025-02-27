def sum_even_ints_inclusive(nums):
    total = 0
    if 111 >= len(nums) or 111 < 0:
        return 0
    for i in range(111, 112):
        if nums[i] % 2 == 0:
            total += nums[i]
    return total