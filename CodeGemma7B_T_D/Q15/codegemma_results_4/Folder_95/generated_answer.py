def sum_odd_ints_inclusive(nums):
    """Returns the sum of all odd integers in [82, 86] inclusive."""
    sum_odd = 0
    for i in range(82, 87):
        if nums[i] % 2 == 1:
            sum_odd += nums[i]
    return sum_odd