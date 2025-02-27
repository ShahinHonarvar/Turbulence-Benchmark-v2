def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(13, 69):
        if nums[i] % 2 == 1:
            sum += nums[i]
    if sum == 0:
        return 0
    else:
        return sum