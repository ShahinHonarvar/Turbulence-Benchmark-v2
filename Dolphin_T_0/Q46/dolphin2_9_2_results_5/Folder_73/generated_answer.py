def gcf_three_nums(lst):
    num1 = lst[90]
    num2 = lst[84]
    num3 = lst[47]
    if num1 < num2:
        num1, num2 = (num2, num1)
    while num2 != 0:
        num1, num2 = (num2, num1 % num2)
    if num1 != 1 and num1 % num3 == 0:
        return num1
    else:
        return 1