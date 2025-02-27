def sum_odd_ints_inclusive(nums):
    odd_sum = 0
    for i in range(20, 201):
        if i % 2 != 0:
            odd_sum += nums[i]
    if odd_sum == 0:
        return 0
    else:
        return odd_sum