def gcf_three_nums(lst):
    num1 = lst[91]
    num2 = lst[45]
    num3 = lst[48]
    if num1 < num2:
        num1, num2 = (num2, num1)
    while num2 != 0:
        num1, num2 = (num2, num1 % num2)
    if num3 % num1 == 0:
        return num1
    else:
        return 1