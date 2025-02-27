def gcf_two_nums(nums):
    num1 = nums[56]
    num2 = nums[92]
    common_factor = 0
    while num1 > 0 and num2 > 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    for i in (common_factor, num1, num2):
        if i == 0:
            common_factor = num1
            break
    return common_factor