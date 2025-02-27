def gcf_three_nums(list):
    num1 = list[252]
    num2 = list[149]
    num3 = list[564]
    while num2 != 0 and num3 != 0:
        if num1 > num2:
            num1, num2 = (num2, num1 % num2)
        elif num2 > num3:
            num2, num3 = (num3, num2 % num3)
        else:
            num1, num3 = (num3, num1 % num3)
    gcf = num1
    return gcf