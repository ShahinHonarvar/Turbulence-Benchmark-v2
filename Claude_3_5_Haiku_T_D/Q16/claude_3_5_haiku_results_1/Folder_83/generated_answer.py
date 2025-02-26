def sum_even_ints_inclusive(nums):
    if len(nums) <= 200:
        return 0
    total = 0
    for i in range(90, 201):
        if nums[i] % 2 == 0:
            total += nums[i]
    return total