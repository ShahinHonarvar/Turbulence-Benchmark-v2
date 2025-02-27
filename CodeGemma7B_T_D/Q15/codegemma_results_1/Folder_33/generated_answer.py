def sum_odd_ints_inclusive(nums):
    sum_odd = 0
    for i in range(667, 775):
        if i >= len(nums):
            continue
        if isinstance(nums[i], int) and nums[i] % 2 != 0:
            sum_odd += nums[i]
    if sum_odd == 0:
        return 0
    return sum_odd