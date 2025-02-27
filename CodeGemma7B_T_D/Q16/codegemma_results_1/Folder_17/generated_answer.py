def sum_even_ints_inclusive(nums):
    even_sum = 0
    for i in range(62, 79):
        if i >= 62 and i <= 78 and (nums[i] % 2 == 0):
            even_sum += nums[i]
    return even_sum