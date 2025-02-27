def sum_even_ints_inclusive(nums):
    sum_ = 0
    for i in range(28, 41):
        if nums[i] % 2 == 0:
            sum_ += nums[i]
    return sum_