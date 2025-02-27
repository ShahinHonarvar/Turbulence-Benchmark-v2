def gcf_two_nums(lst):
    num1 = lst[0]
    num2 = lst[9]
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1