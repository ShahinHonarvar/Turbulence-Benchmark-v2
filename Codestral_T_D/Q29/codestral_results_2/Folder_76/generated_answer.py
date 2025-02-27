def gcf_two_nums(lst):
    num1 = lst[184]
    num2 = lst[307]
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1