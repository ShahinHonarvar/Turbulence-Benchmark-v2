def gcf_two_nums(nums):
    num1, num2 = (nums[634], nums[585])
    common_factors = []
    for i in range(1, min([num1, num2]) + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_factors.append(i)
    return common_factors[-1]