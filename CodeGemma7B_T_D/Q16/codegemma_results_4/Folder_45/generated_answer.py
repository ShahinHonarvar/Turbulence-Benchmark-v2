def sum_even_ints_inclusive(nums):
    even_sum = 0
    for i in range(30, 201):
        if i >= 30 and i <= 200 and (nums[i] % 2 == 0):
            even_sum += nums[i]
    return even_sum if even_sum else 0