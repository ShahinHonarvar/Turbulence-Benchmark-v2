def sum_even_ints_inclusive(nums):
    _sum = 0
    for i in range(62, 93):
        if nums[i] % 2 == 0:
            _sum += nums[i]
    return _sum