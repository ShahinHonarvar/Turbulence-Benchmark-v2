def gcf_two_nums(nums):
    num1, num2 = (nums[17], nums[20])
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    while smaller > 0:
        if num1 % smaller == 0 and num2 % smaller == 0:
            gcf = smaller
            break
        smaller -= 1
    return gcf