def gcf_two_nums(li):
    num1 = li[76]
    num2 = li[57]
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1