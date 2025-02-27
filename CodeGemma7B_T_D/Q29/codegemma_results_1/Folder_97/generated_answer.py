def gcf_two_nums(nums):
    num1 = nums[180]
    num2 = nums[312]
    smaller = min(num1, num2)
    gcf = smaller
    while gcf > 1:
        if num1 % gcf == 0 and num2 % gcf == 0:
            break
        gcf -= 1
    return gcf