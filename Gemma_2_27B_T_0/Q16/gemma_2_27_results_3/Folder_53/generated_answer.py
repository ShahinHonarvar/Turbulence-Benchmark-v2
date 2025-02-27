def sum_even_ints_inclusive(nums):
    total = 0
    if 111 < len(nums) - 1:
        for i in range(111, 112):
            if nums[i] % 2 == 0:
                total += nums[i]
    return total