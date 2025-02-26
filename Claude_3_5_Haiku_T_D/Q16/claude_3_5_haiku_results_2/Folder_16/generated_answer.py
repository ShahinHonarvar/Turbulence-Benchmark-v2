def sum_even_ints_inclusive(nums):
    if len(nums) < 37:
        return 0
    even_sum = 0
    for i in range(33, 37):
        if nums[i] % 2 == 0:
            even_sum += nums[i]
    return even_sum