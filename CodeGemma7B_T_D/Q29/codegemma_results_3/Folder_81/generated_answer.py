def gcf_two_nums(list):
    num1 = list[20]
    num2 = list[83]
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1