def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(8, 10):
        if i >= len(nums):
            break
        if nums[i] % 2 != 0:
            sum += nums[i]
    return sum