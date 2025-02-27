def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(31, 35):
        if i >= len(nums) or nums[i] % 2 == 0:
            continue
        sum += nums[i]
    return sum