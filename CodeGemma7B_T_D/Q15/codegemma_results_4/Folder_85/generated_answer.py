def sum_odd_ints_inclusive(nums):
    sum_odd = 0
    for i in range(6, 9):
        if i >= 0 and i <= len(nums) - 1 and (nums[i] % 2 != 0):
            sum_odd += nums[i]
    if sum_odd == 0:
        return -1
    return sum_odd