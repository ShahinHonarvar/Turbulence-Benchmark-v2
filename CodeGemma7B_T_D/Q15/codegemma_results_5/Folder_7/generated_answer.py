def sum_odd_ints_inclusive(nums):
    total_sum = 0
    for i in range(661, 925):
        if i % 2 != 0:
            total_sum += nums[i]
    return total_sum if total_sum else 0