def sum_odd_ints_inclusive(nums):
    sum_odd_ints = 0
    for i in range(55, 99):
        if i >= len(nums) or i < 0:
            continue
        elif nums[i] % 2 != 0:
            sum_odd_ints += nums[i]
    return sum_odd_ints