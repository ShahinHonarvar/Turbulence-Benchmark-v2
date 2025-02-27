def gcf_two_nums(lst):
    num1 = lst[36]
    num2 = lst[85]
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1