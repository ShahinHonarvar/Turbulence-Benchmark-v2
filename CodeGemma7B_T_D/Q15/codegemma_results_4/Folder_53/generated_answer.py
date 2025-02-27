def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(300, 301):
        if nums[i] % 2 == 1:
            sum += nums[i]
    return sum if sum != 0 else 0