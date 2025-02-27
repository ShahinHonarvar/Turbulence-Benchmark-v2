def gcf_two_nums(lst):
    num1 = lst[129]
    num2 = lst[582]
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1