def sum_even_ints_inclusive(nums):
    even_sum = 0
    for i in range(min(5, len(nums))):
        if nums[i] % 2 == 0:
            even_sum += nums[i]
    return even_sum