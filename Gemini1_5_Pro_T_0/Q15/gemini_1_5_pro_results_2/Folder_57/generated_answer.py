def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(max(27, 0), min(len(nums), 56)):
        if nums[i] % 2 != 0:
            sum += nums[i]
    return sum