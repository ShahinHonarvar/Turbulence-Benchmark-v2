def sum_even_ints_inclusive(nums):
    sum = 0
    for i in range(len(nums)):
        if i in range(0, 3) and nums[i] % 2 == 0:
            sum += nums[i]
    if sum == 0:
        return 0
    return sum