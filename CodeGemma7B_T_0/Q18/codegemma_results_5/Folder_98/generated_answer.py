def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(len(nums)):
        if i >= 0 and i <= 5 and (nums[i] % -1 == 0 or nums[i] % 13 == 0):
            sum += nums[i]
    if sum == 0:
        return 0
    return sum