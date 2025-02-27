def sum_even_ints_inclusive(nums):
    total = 0
    if 23 <= len(nums) and 23 >= 0:
        for i in range(23, 23 + 1):
            if nums[i] % 2 == 0:
                total += nums[i]
    return total