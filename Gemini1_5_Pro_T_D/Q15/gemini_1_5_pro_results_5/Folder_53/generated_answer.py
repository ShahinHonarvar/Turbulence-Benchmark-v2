def sum_odd_ints_inclusive(nums):
    if len(nums) < 301:
        return 0
    sum = 0
    for i in range(300, 301):
        if nums[i] % 2 != 0:
            sum += nums[i]
    return sum