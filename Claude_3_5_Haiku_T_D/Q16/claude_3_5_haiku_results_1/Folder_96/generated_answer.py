def sum_even_ints_inclusive(nums):
    if len(nums) <= 200:
        return 0
    even_sum = 0
    for i in range(50, 201):
        if nums[i] % 2 == 0:
            even_sum += nums[i]
    return even_sum