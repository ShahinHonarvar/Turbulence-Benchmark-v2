def sum_even_ints_inclusive(nums):
    even_sum = 0
    for i in range(22, 89):
        if i >= 22 and i <= 88 and (nums[i] % 2 == 0):
            even_sum += nums[i]
    return even_sum or 0