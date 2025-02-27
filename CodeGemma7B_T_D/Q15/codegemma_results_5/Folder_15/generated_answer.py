def sum_odd_ints_inclusive(nums):
    sum_odd = 0
    for i in range(4):
        if nums[i] % 2 == 1:
            sum_odd += nums[i]
    if not sum_odd:
        return 0
    return sum_odd