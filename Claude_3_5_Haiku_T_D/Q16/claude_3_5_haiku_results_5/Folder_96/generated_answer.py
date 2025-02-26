def sum_even_ints_inclusive(nums):
    even_sum = 0
    for index in range(50, 201):
        if index < len(nums) and nums[index] % 2 == 0:
            even_sum += nums[index]
    return even_sum