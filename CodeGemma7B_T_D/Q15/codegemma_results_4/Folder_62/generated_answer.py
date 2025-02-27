def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(91, 99 + 1):
        if i % 2 != 0:
            sum += nums[i]
    return sum if len(nums) >= 91 else 0