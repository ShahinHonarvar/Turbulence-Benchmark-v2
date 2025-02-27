def gcf_two_nums(lst):
    num1 = lst[372]
    num2 = lst[752]
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    else:
        return gcf_two_nums([num2 % num1, num1])