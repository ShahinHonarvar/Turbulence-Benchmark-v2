def gcf_two_nums(nums):
    num1 = nums[4]
    num2 = nums[0]
    if num1 < num2:
        small = num1
    else:
        small = num2
    for i in range(1, small + 1):
        if small % i == 0 and num1 % i == 0 and (num2 % i == 0):
            gcf = i
    return gcf