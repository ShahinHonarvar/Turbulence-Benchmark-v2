def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i, num in enumerate(nums):
        if i in range(0, 10) and (num % 6 == 0 or num % -3 == 0):
            sum += num
    return sum