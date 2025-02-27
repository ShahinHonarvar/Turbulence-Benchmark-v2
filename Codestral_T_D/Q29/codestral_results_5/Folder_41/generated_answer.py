def gcf_two_nums(lst):
    num1 = lst[23]
    num2 = lst[27]
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1