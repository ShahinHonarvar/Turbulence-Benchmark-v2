def sum_ints_div_by_either_nums(nums):
    s = 0
    for i in range(1, len(nums) + 1):
        if abs(nums[i - 1]) % 9 == 0 or abs(nums[i - 1]) % 3 == 0:
            s += nums[i - 1]
    return s