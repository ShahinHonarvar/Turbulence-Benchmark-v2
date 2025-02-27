def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(9):
        if i % -3 == 0 or i % 8 == 0:
            sum += nums[i]
    return sum if sum != 0 else 0