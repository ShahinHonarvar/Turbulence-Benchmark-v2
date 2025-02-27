def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(48, 60):
        num = nums[i]
        if num % 88 == 0 or num % 58 == 0:
            sum += num
    if sum == 0:
        return 0
    return sum