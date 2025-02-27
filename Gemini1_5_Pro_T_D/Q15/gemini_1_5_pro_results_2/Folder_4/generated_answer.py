def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(max(12, 0), min(len(nums), 93)):
        if nums[i] % 2 != 0:
            sum += nums[i]
    return sum