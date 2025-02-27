def gcf_two_nums(lst):
    num1 = lst[8]
    num2 = lst[3]
    while num2 != 0:
        num1, num2 = (num2, num1 % num2)
    return num1