def sum_even_ints_inclusive(nums):
    even_sum = 0
    for i in range(3):
        if i >= 0 and i < len(nums) and (nums[i] % 2 == 0):
            even_sum += nums[i]
    return even_sum