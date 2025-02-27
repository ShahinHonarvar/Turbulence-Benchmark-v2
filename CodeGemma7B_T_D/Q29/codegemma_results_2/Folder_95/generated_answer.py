def gcf_two_nums(lst):
    num1 = lst[43]
    num2 = lst[99]
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1