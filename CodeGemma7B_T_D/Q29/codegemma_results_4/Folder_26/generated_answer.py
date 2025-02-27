def gcf_two_nums(lst):
    num1, num2 = (lst[49], lst[31])
    temp = num1 % num2
    while temp != 0:
        num1, num2 = (num2, temp)
        temp = num1 % num2
    return num2