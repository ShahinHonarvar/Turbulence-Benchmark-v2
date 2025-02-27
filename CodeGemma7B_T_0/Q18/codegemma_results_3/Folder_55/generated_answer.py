def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(len(nums)):
        if i >= 0 and i <= 9 and (nums[i] % 10 == 0 or nums[i] % 100 == 0):
            sum += nums[i]
    return sum