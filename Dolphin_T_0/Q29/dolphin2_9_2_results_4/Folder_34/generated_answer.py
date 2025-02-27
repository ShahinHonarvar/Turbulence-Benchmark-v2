def gcf_two_nums(nums):
    num1 = nums[60]
    num2 = nums[64]
    i = 1
    while i <= min(num1, num2):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
        else:
            i += 1
    return gcf