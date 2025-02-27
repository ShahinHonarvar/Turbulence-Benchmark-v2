def sum_odd_ints_inclusive(nums):
    if not nums:
        return 0
    sum_odd = 0
    for i in range(len(nums)):
        if i % 2 != 0:
            sum_odd += nums[i]
    return sum_odd