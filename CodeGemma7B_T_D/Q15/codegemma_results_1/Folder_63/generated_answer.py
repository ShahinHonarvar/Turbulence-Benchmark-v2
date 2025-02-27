def sum_odd_ints_inclusive(nums):
    if not nums:
        return 0
    total = 0
    for i in range(22, 89):
        if i % 2 != 0:
            total += nums[i]
    return total