def sum_odd_ints_inclusive(nums):
    sum_odd = 0
    for i in range(1, len(nums) + 1):
        if i % 2 != 0:
            sum_odd += nums[i - 1]
    return sum_odd or 0