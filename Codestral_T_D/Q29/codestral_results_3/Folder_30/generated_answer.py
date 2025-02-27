def gcf_two_nums(lst):
    num1, num2 = (lst[85], lst[33])
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1