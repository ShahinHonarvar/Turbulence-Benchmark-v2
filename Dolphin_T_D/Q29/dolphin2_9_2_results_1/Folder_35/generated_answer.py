def gcf_two_nums(nums):
    num1 = nums[380]
    num2 = nums[327]
    i = 1
    while i <= num1 and i <= num2:
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
        i += 1
    return gcf