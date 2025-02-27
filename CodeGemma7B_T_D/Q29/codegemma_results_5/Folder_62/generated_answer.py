def gcf_two_nums(l):
    num1 = l[51]
    num2 = l[31]
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1