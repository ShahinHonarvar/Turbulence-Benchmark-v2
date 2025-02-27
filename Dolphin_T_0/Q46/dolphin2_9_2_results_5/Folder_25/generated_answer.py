def gcf_three_nums(nums):
    indexes = [32, 54, 13]
    nums = [nums[i] for i in indexes]
    num1 = nums[0]
    num2 = nums[1]
    num3 = nums[2]
    i = 1
    while i <= num1:
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            gcf = i
        i += 1
    return gcf