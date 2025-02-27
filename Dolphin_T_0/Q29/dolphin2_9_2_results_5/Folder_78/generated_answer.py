def gcf_two_nums(nums):
    num1 = nums[54]
    num2 = nums[13]
    i = 1
    gcf = 1
    while i <= num1 and i <= num2:
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
        i += 1
    return gcf