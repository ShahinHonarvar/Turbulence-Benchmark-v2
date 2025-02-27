def gcf_three_nums(three_nums):
    num1, num2, num3 = (three_nums[76], three_nums[64], three_nums[28])
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1