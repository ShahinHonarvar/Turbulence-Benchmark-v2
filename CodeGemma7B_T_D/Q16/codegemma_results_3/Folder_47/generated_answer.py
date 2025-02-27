def sum_even_ints_inclusive(nums):
    total = 0
    i = 37
    while i <= 76 and len(nums) > i:
        if nums[i] % 2 == 0:
            total += nums[i]
        i += 1
    return total