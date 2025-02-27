def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(1, len(nums) + 1):
        if i % 2 != 0:
            sum += nums[i - 1]
    return sum