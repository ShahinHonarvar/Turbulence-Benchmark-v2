def gcf_three_nums(lst):
    num1 = lst[76]
    num2 = lst[64]
    num3 = lst[28]
    if num1 < num2:
        num1, num2 = (num2, num1)
    if num1 < num3:
        num1, num3 = (num3, num1)
    while num3 != 0:
        temp = num3
        num3 = num1 % num3
        num1 = num2 % num1
        num2 = temp
    return num1