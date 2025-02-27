def sum_odd_ints_inclusive(nums):
    _sum = 0
    for i in range(23, 24):
        if nums[i] % 2 == 1:
            _sum += nums[i]
    return _sum