def sum_odd_ints_inclusive(nums):
    for i in range(55, 99):
        if nums[i] % 2 == 1:
            result += nums[i]
    return result if result else 0