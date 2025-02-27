def sum_ints_div_by_either_nums(nums):
    sum = 0
    for i in range(70, 201):
        num = nums[i]
        if num % 3 == 0 or num % -300 == 0:
            sum += num
    return sum