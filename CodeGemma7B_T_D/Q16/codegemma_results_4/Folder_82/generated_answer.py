def sum_even_ints_inclusive(nums):
    sum = 0
    for i in range(len(nums)):
        if i >= 29 and i <= 29 and (nums[i] % 2 == 0):
            sum += nums[i]
    if sum == 0:
        return 0
    else:
        return sum