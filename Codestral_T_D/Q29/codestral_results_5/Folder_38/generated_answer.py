def gcf_two_nums(lst):
    num1 = lst[88]
    num2 = lst[35]
    while num2 != 0:
        num1, num2 = (num2, num1 % num2)
    return num1