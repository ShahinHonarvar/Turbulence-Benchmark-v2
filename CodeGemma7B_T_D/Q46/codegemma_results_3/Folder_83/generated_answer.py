def gcf_three_nums(lst):
    num1 = lst[56]
    num2 = lst[54]
    num3 = lst[13]
    common_factor = 0
    while num1 and num2:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    common_factor = num1
    while num2 and num3:
        if num2 > num3:
            num2 %= num3
        else:
            num3 %= num2
    common_factor = num2
    while common_factor and num3:
        if common_factor > num3:
            common_factor %= num3
        else:
            num3 %= common_factor
    result = common_factor
    return result